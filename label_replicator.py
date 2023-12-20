import requests

def get_labels(source_repo, token):
  """Fetch labels from the source repository."""
  headers = {'Authorization': f'token {token}'}
  response = requests.get(f'https://api.github.com/repos/{source_repo}/labels', headers=headers)
  return response.json()

def create_label(target_repo, token, label):
  """Create a label in the target repository."""
  headers = {'Authorization': f'token {token}', 'Content-Type': 'application/json'}
  response = requests.post(f'https://api.github.com/repos/{target_repo}/labels', json=label, headers=headers)
  return response

def replicate_labels(source_repo, target_repo, token):
  """Replicate labels from source repo to target repo."""
  labels = get_labels(source_repo, token)
  for label in labels:
      create_label(target_repo, token, label)
      print(f"Label '{label['name']}' replicated to {target_repo}")

if __name__ == "__main__":
  source_repo = input("Enter the source repository (username/repo): ")
  target_repo = input("Enter the target repository (username/repo): ")
  github_token = input("Enter your GitHub token: ")

  replicate_labels(source_repo, target_repo, github_token)
