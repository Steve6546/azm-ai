<a name="readme-top"></a>

<div align="center">
  <img src="./docs/static/img/logo.png" alt="Logo" width="200">
  <h1 align="center">AZM AI: Advanced AI Development Platform</h1>
</div>


<div align="center">
  <a href="https://github.com/Steve6546/azm-ai/graphs/contributors"><img src="https://img.shields.io/github/contributors/Steve6546/azm-ai?style=for-the-badge&color=blue" alt="Contributors"></a>
  <a href="https://github.com/Steve6546/azm-ai/stargazers"><img src="https://img.shields.io/github/stars/Steve6546/azm-ai?style=for-the-badge&color=blue" alt="Stargazers"></a>
  <a href="https://github.com/Steve6546/azm-ai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Steve6546/azm-ai?style=for-the-badge&color=blue" alt="MIT License"></a>
  <br/>
  <a href="https://github.com/Steve6546/azm-ai/blob/main/CREDITS.md"><img src="https://img.shields.io/badge/Project-Credits-blue?style=for-the-badge&color=FFE165&logo=github&logoColor=white" alt="Credits"></a>
  <br/>
  <a href="https://github.com/Steve6546/azm-ai/wiki"><img src="https://img.shields.io/badge/Documentation-000?logo=googledocs&logoColor=FFE165&style=for-the-badge" alt="Check out the documentation"></a>
  <a href="https://github.com/Steve6546/azm-ai"><img src="https://img.shields.io/badge/AZM%20AI-000?logoColor=FFE165&logo=github&style=for-the-badge" alt="AZM AI"></a>
  <hr>
</div>

Welcome to AZM AI, an advanced platform for software development agents powered by AI.

AZM AI agents can do anything a human developer can: modify code, run commands, browse the web,
call APIs, and yes—even copy code snippets from StackOverflow.

Learn more in our [GitHub Wiki](https://github.com/Steve6546/azm-ai/wiki) to get started.

> [!IMPORTANT]
> Using AZM AI for work? We'd love to chat! Contact us at
> [Steve6546](https://github.com/Steve6546)
> to learn more about our services and how AZM AI can help your business.

![App screenshot](./docs/static/img/screenshot.png)

## ☁️ AZM AI Cloud
The easiest way to get started with AZM AI is on our cloud platform,
contact us to learn more about our cloud offerings.

## 💻 Running AZM AI Locally

AZM AI can also run on your local system using Docker.
See our [Wiki](https://github.com/Steve6546/azm-ai/wiki) for
system requirements and more information.

> [!WARNING]
> On a public network? See our [Security Guide](https://github.com/Steve6546/azm-ai/wiki/Security)
> to secure your deployment by restricting network binding and implementing additional security measures.


```bash
docker pull ghcr.io/steve6546/azm-ai/runtime:latest

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=ghcr.io/steve6546/azm-ai/runtime:latest \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.azm-ai-state:/.azm-ai-state \
    -p 3000:3000 \
    -p 12001:12001 \
    --add-host host.docker.internal:host-gateway \
    --name azm-ai-app \
    ghcr.io/steve6546/azm-ai/azm-ai:latest
```

You'll find AZM AI running at [http://localhost:3000](http://localhost:3000)!

When you open the application, you'll be asked to choose an LLM provider and add an API key.
[Anthropic's Claude 3.5 Sonnet](https://www.anthropic.com/api) (`anthropic/claude-3-5-sonnet-20241022`)
works best, but you have many options available.

## 💡 Other ways to run AZM AI

> [!CAUTION]
> AZM AI is meant to be run by a single user on their local workstation.
> It is not appropriate for multi-tenant deployments where multiple users share the same instance. There is no built-in authentication, isolation, or scalability.
>
> If you're interested in running AZM AI in a multi-tenant environment, please
> [contact us](https://github.com/Steve6546)
> for advanced deployment options.

You can also connect AZM AI to your local filesystem,
run AZM AI in a scriptable headless mode,
interact with it via a friendly CLI,
or run it on tagged issues with a github action.

Visit our Wiki for more information and setup instructions.

If you want to modify the AZM AI source code, check out [Development.md](https://github.com/Steve6546/azm-ai/blob/main/Development.md).

Having issues? Check our Troubleshooting Guide in the Wiki.

## 📖 Documentation

To learn more about the project, and for tips on using AZM AI,
check out our [documentation](https://github.com/Steve6546/azm-ai/wiki).

There you'll find resources on how to use different LLM providers,
troubleshooting resources, and advanced configuration options.

## 🤝 How to Join the Community

AZM AI is a community-driven project, and we welcome contributions from everyone. We do most of our communication
through GitHub, so this is the best place to start:

- [Read or post Github Issues](https://github.com/Steve6546/azm-ai/issues) - Check out the issues we're working on, or add your own ideas.
- [Contact us directly](https://github.com/Steve6546) - For business inquiries or partnership opportunities.

See more about the community in [COMMUNITY.md](./COMMUNITY.md) or find details on contributing in [CONTRIBUTING.md](./CONTRIBUTING.md).

## 📈 Progress

See the AZM AI roadmap [here](https://github.com/Steve6546/azm-ai/projects) for our upcoming features and improvements.

<p align="center">
  <a href="https://star-history.com/#Steve6546/azm-ai&Date">
    <img src="https://api.star-history.com/svg?repos=Steve6546/azm-ai&type=Date" width="500" alt="Star History Chart">
  </a>
</p>

## 📜 License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

## 🙏 Acknowledgements

AZM AI is built by a dedicated team of contributors, and every contribution is greatly appreciated! 

AZM AI is an advanced AI development platform built under the MIT license. We've created a comprehensive solution with innovative features and capabilities to enhance AI-driven development workflows.

For a list of open source projects and licenses used in AZM AI, please see our [CREDITS.md](./CREDITS.md) file.

## 📚 References

AZM AI is based on advanced AI research and development in the field of generalist agents for software development.

## 🏗️ Project Structure

AZM AI is organized into several key components:

### Core Components

- **azm_ai/core**: Core functionality and configuration
- **azm_ai/events**: Event handling system for actions and observations
- **azm_ai/runtime**: Runtime environments for executing agent actions
  - **impl/modal**: High-availability runtime implementation
  - **impl/e2b**: File system operations implementation
  - **impl/browsergym**: Web browsing capabilities
- **azm_ai/server**: Server implementation including API endpoints and middleware
- **azm_ai/storage**: Data persistence layer
- **azm_ai/utils**: Utility functions used throughout the codebase

### Frontend

- **frontend**: React-based user interface
  - **src/components**: UI components
  - **src/pages**: Application pages
  - **src/hooks**: Custom React hooks
  - **src/utils**: Frontend utility functions

### Testing

- **tests**: Comprehensive test suite
  - **unit**: Unit tests for individual components
  - **integration**: Integration tests for component interactions
  - **e2e**: End-to-end tests for complete workflows

### Documentation

- **docs**: Project documentation
  - **static**: Static assets including images
  - **api**: API documentation
  - **guides**: User and developer guides

## 🧩 Architecture

AZM AI follows a modular architecture with clear separation of concerns:

1. **Event-Driven Core**: The system is built around an event stream that handles actions and observations
2. **Pluggable Runtimes**: Different runtime environments can be used for executing actions
3. **Extensible API**: The server exposes a RESTful API for interacting with the system
4. **Responsive UI**: The frontend provides a user-friendly interface for interacting with AI agents

This architecture allows for easy extension and customization of the platform for different use cases.