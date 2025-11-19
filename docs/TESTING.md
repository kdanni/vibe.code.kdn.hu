# Testing Philosophy and Workflow

## 🧪 Vibe-Based Testing

In alignment with the "Vibe Coding" philosophy, our testing approach is designed to be lightweight, flexible, and focused on verifying the intended "vibe" of the application rather than on traditional, fine-grained unit testing.

The primary goal of our testing is to answer the question: **"Does the generated code (the 'slop') do what I intended it to do?"**

## 🛠️ Tools

We will use `pytest` for our testing framework due to its simplicity, flexibility, and powerful features. To install `pytest`, run:

```bash
pip install pytest
```

##  workflow

1.  ***Test Directory***: All tests will be located in the `tests/` directory at the root of the repository.

2.  ***Sanity Check***: A sanity check test will be included to ensure that the environment is configured correctly and that `pytest` is working as expected.

3.  ***Vibe Checks***: For each new "vibe" (i.e., each new prompt and its corresponding "slop"), a corresponding test file will be created in the `tests/` directory. For example, for `prompts/p001_basic_cli_tool.md`, the corresponding test file would be `tests/test_p001.py`.

4.  ***Running Tests***: To run the tests, simply run the `pytest` command from the root of the repository:

    ```bash
    pytest
    ```

5.  ***Continuous Integration***: In the future, we may integrate our tests into a CI/CD pipeline to automatically run our "vibe checks" on each new commit.
