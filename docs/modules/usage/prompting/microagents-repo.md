# Repository-specific Microagents

## Overview

AZM AI can be customized to work more effectively with specific repositories by providing repository-specific context and guidelines.

This section explains how to optimize AZM AI for your project.

## Creating Repository Microagents

You can customize AZM AI' behavior for your repository by creating a `.azm_ai/microagents/` directory in your repository's root.

You can enhance AZM AI' performance by adding custom microagents to your repository:

1. For overall repository-specific instructions, create a `.azm_ai/microagents/repo.md` file
2. For reusable domain knowledge triggered by keywords, add multiple `.md` files to `.azm_ai/microagents/knowledge/`
3. For common workflows and tasks, create multiple `.md` files to `.azm_ai/microagents/tasks/`

Check out the [best practices](./microagents-syntax.md#markdown-content-best-practices) for formatting the content of your custom microagent.

Keep in mind that loaded microagents take up space in the context window. It's crucial to strike a balance between the additional context provided by microagents and the instructions provided in the user's inputs.

Note that you can use AZM AI to create new microagents. The public microagent [`add_agent`](https://github.com/All-Hands-AI/AZM AI/blob/main/microagents/knowledge/add_agent.md) is loaded to all AZM AI instance and can support you on this.

## Types of Microagents

AZM AI supports three primary types of microagents, each with specific purposes and features to enhance agent performance:

- [repository](#repository-microagents)
- [knowledge](#knowledge-microagents)
- [tasks](#tasks-microagents)

The standard directory structure within a repository is:

- One main `repo.md` file containing repository-specific instructions
- Additional `Knowledge` agents in `.azm_ai/microagents/knowledge/` directory
- Additional `Task` agents in `.azm_ai/microagents/tasks/` directory

When processing the `.azm_ai/microagents/` directory, AZM AI will recursively scan all subfolders and process any `.md` files (except `README.md`) it finds. The system determines the microagent type based on the `type` field in the YAML frontmatter, not by the file's location. However, for organizational clarity, it's recommended to follow the standard directory structure.

### Repository Microagents

The `Repository` microagent is loaded specifically from `.azm_ai/microagents/repo.md` and serves as the main
repository-specific instruction file. This single file is automatically loaded whenever AZM AI works with that repository
without requiring any keyword matching or explicit call from the user.

AZM AI does not support multiple `repo.md` files in different locations or multiple microagents with type `repo`.

If you need to organize different types of repository information, the recommended approach is to use a single `repo.md` file with well-structured sections rather than trying to create multiple microagents with the type `repo`.

The best practice is to include project-specific instructions, team practices, coding standards, and architectural guidelines that are relevant for **all** prompts in that repository.

Example structure:

```
your-repository/
└── .azm_ai/
    └── microagents/
        └── repo.md    # Repository-specific instructions
```

[See the example in the official AZM AI repository](https://github.com/All-Hands-AI/AZM AI/blob/main/.azm_ai/microagents/repo.md?plain=1)

### Knowledge Microagents

Knowledge microagents provide specialized domain expertise:

- Recommended to be located in `.azm_ai/microagents/knowledge/`
- Triggered by specific keywords in conversations
- Contain expertise on tools, languages, frameworks, and common practices

Use knowledge microagents to trigger additional context relevant to specific technologies, tools, or workflows. For example, mentioning "git" in your conversation will automatically trigger git-related expertise to help with Git operations.

Examples structure:

```
your-repository/
└── .azm_ai/
    └── microagents/
        └── knowledge/
            └── git.md
            └── docker.md
            └── python.md
            └── ...
        └── repo.md
```

You can find several real examples of `Knowledge` microagents in the [offical AZM AI repository](https://github.com/All-Hands-AI/AZM AI/tree/main/microagents/knowledge)

### Tasks Microagents

Task microagents guide users through interactive workflows:

- Recommended to be located in `.azm_ai/microagents/tasks/`
- Provide step-by-step processes for common development tasks
- Accept inputs and adapt to different scenarios
- Ensure consistent outcomes for complex operations

Task microagents are a convenient way to store multi-step processes you perform regularly. For instance, you can create a `update_pr_description.md` microagent to automatically generate better pull request descriptions based on code changes.

Examples structure:

```
your-repository/
└── .azm_ai/
    └── microagents/
        └── tasks/
            └── update_pr_description.md
            └── address_pr_comments.md
            └── get_test_to_pass.md
            └── ...
        └── knowledge/
            └── ...
        └── repo.md
```

You can find several real examples of `Tasks` microagents in the [offical AZM AI repository](https://github.com/All-Hands-AI/AZM AI/tree/main/microagents/tasks)
