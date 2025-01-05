# GitHub Spider

This project is an auto spider that collects a user's followers and followings on GitHub using Python. The collected data is saved as JSON files.

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   ```
2. Navigate to the project directory:
   ```
   cd workspace-blank
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the script:
   ```
   python github_spider.py <github_username> <layers>
   ```
5. The followers and followings data will be saved as `followers.json` and `followings.json` respectively in the project directory.

## Example

To recursively obtain a person's follower list and following list up to 2 layers, run the following command:

```
python github_spider.py octocat 2
```

# Note

This is a project to try using [copilot-workspace](https://copilot-workspace.githubnext.com/).
