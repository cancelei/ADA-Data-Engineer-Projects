import requests
import csv
import zipfile
import io
import re
import os

# Constants
REPO_OWNER = "rubyforgood"
REPO_NAME = "human-essentials"
GITHUB_TOKEN = "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"  # Use your GitHub token here
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
WORKFLOW_FILES = [
    "add-help-wanted-labels.yml", "brakeman.yml", "factory-bot-lint.yml",
    "issue-auto-unassign.yml", "plantuml.yml", "release-notifier.yml",
    "remove-help-wanted-labels-done.yml", "remove-help-wanted-labels-in-progress.yml",
    "remove-help-wanted-labels-merged-to-qa.yml", "remove-help-wanted.yml",
    "rspec-events.yml", "rspec-system-events.yml", "rspec-system.yml",
    "rspec.yml", "ruby_lint.yml"
]
CSV_FILE = "ci_run_metadata_per_workflow.csv"

def fetch_workflow_runs(workflow_file):
    API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{workflow_file}/runs"
    params = {"per_page": 20}
    response = requests.get(API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()['workflow_runs']

def save_runs_to_csv(data):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:  # Use 'a' to append to the file
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def parse_rspec_failures(log_content):
    # Adjust the regular expression as needed
    failure_pattern = re.compile(r'Failures:\n\n(?:\d+)\) (.+?)\n\s+Failure/Error: (.+?)(?:\n\n|\Z)', re.DOTALL)
    matches = failure_pattern.findall(log_content)
    failures = [{'test': match[0], 'error': match[1]} for match in matches]
    return failures

def save_rspec_failures_to_csv(failures, csv_file='rspec_failures.csv'):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Test", "Error Message"])
        for failure in failures:
            writer.writerow([failure['test'], failure['error']])


def download_and_extract_log(run_id):
    log_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}/logs"
    response = requests.get(log_url, headers=HEADERS, stream=True)
    
    if response.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(f"./logs/{run_id}")
        print(f"Logs extracted for run ID: {run_id}")
        return f"./logs/{run_id}"
    else:
        print(f"Failed to download logs for run ID: {run_id}")
        return None


def main():
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Workflow File", "Run ID", "Workflow Name", "Status", "Conclusion"])
    
    rspec_failures = []
    for workflow_file in WORKFLOW_FILES:
        runs = fetch_workflow_runs(workflow_file)
        failed_runs = [run for run in runs if run['conclusion'] != 'success']
        for run in failed_runs:
            log_dir = download_and_extract_log(run['id'])
            if log_dir:
                # Ensure to process only files within the directory
                for filename in os.listdir(log_dir):
                    file_path = os.path.join(log_dir, filename)
                    if os.path.isfile(file_path):  # Check if the path is a file
                        with open(file_path, 'r', encoding='utf-8') as log_file:
                            log_content = log_file.read()
                            failures = parse_rspec_failures(log_content)
                            rspec_failures.extend(failures)
                            # Save metadata about the run
                            data = [[workflow_file, run['id'], run['name'], run['status'], run['conclusion']]]
                            save_runs_to_csv(data)
    
    # After collecting all RSpec failures, save them to a CSV file
    save_rspec_failures_to_csv(rspec_failures)

if __name__ == "__main__":
    main()