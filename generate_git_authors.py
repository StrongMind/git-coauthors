import json
import os
from os.path import exists


def main():
    home_path = os.path.expanduser('~')
    with open('git-coauthors.json', 'r') as git_coauthors_file:
        git_coauthors_data = json.load(git_coauthors_file)
    git_coauthors_data_add = {}
    if exists('git-coauthors-addendum.json'):
        with open('git-coauthors-addendum.json', 'r') as git_coauthors_addendum_file:
            git_coauthors_data_add = json.loads(git_coauthors_addendum_file.read())

    git_coauthors_override_data = {}

    if exists('git-coauthors-override.json'):
        with open('git-coauthors-override.json', 'r') as git_coauthors_override_file:
            git_coauthors_override_data = json.loads(git_coauthors_override_file.read())
    git_coauthors_addendum = []
    if git_coauthors_data_add:
        git_coauthors_addendum = git_coauthors_data_add.get('coauthors', [])
    git_coauthors_flat = []
    git_coauthors = {}
    for author in git_coauthors_data['coauthors'] + git_coauthors_addendum:
        name = author['name']
        email = author['email']
        names = name.split(' ')
        first_chars = [(item[0]).lower() for item in names]
        initials = git_coauthors_override_data.get(email, ''.join(first_chars))
        git_coauthors_flat.append(f"{name} <{email}>")
        git_coauthors[initials] = {
            "name": name,
            "email": email
        }

    with open(f'{home_path}/.git_coauthors', 'w') as dot_git_coauthors_flat:
        dot_git_coauthors_flat.writelines('\n'.join(git_coauthors_flat))

    with open(f'{home_path}/.git-coauthors', 'w') as dot_git_tac_coauthors_file:
        dot_git_tac_coauthors_file.write(json.dumps({
            "coauthors": git_coauthors
        }, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
