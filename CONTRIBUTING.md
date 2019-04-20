# Contributing
Welcome! :tada: Thanks you for taking the time to contribute.

## Issues
These are where you report issues or bugs, request features, and stuff like that.

New to issues? Follow [this](https://help.github.com/en/articles/about-issues) link.

## PRs
This is where you make changes to the project and submit them to review by the repo owner (me).

New to PRs? Follow [this](http://makeapullrequest.com) link.

### Ideas
Some PRs I would love to see:

    - Fix python 3.5 support (as it hasn't quite reached EOL and I somehow broke support a few commits ago. See [here](https://travis-ci.org/extremepayne/py-generate-ascii/jobs/520915703) for the broken build).

### Suggestions
To increase the chances of your PR being accepted, follow these suggestions:

    - Lint with pylint, pycodestyle, and pydocstyle.
    - Use windows (CR LF) line endings.

### Requirements
Your PR will not be accepted if it does not follow these requirements:

    - The Travis build passes.
    - Is both Windows, macOS and Linux compatible (will be tested by Travis.).
    - It's formatted with [black](https://github.com/ambv/black).
    - It doesn't expand the scope of the project beyond what I am comfortable managing (I will be the judge of this, if you're unsure just go ahead and submit it anyway).
