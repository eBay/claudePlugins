# claudePlugins

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A single repository to manage all Claude Code plugins.

## Available Plugins

### 1. Frontend Developer Plugin
**Path**: `plugins/frontend-developer`

Specialized agent for generating modern frontend components and scaffolding projects (React, Vue, etc.).

**Features**:
- React/NextJS component creation
- TypeScript/JavaScript expertise
- Tailwind/CSS styling
- Performance optimization
- Accessibility compliance

**Usage**: `/frontend-developer:frontend-developer`

### 2. Java Developer Plugin
**Path**: `plugins/backend-java-developer`

Specialized agent for generating modern Java code with focus on backend development.

**Features**:
- Java, Spring Boot, microservices
- Complex algorithms and data structures
- Database integration (JPA, Hibernate)
- Testing (JUnit, Mockito)
- Enterprise architecture patterns

**Usage**: `/java-developer:java-developer`

### 3. MCP Launcher Wrapper Plugin
**Path**: `plugins/mcp-launcher-wrapper`

MCP server launcher wrapper scripts for managing and monitoring MCP servers in the background with daemon support.

**Features**:
- Background execution of MCP servers with stdio protocol support
- Automatic restart on server failures (daemon mode)
- Process management (start, stop, restart, status)
- Log monitoring and viewing
- FIFO-based stdin management
- Cleanup utilities for orphaned processes
- Fully configurable server definitions

**Usage**: `/mcp-launcher-manager` or direct script execution

See [plugins/mcp-launcher-wrapper/README.md](plugins/mcp-launcher-wrapper/README.md) for detailed setup and configuration.

### 4. Notification Hook Plugin
**Path**: `plugins/notification-hook`

Hook that plays a sound notification when Claude sends notifications.

**Features**:
- Plays a pleasant chime sound on notifications
- Non-blocking audio playback
- Cross-platform Python-based implementation
- Easy to customize with your own sounds

**Setup**:
1. Install plugin to `~/.claude/plugins/notification-hook`
2. Create Python virtual environment and install playsound3
3. Configure hook in `~/.claude/settings.json`

See [plugins/notification-hook/README.md](plugins/notification-hook/README.md) for detailed setup instructions.

### 5. Sanity Check Reviewer Plugin
**Path**: `plugins/sanity-check-reviewer`

Specialized agent for performing rigorous security and performance audits on newly written or modified code before creating PRs.

**Features**:
- Security vulnerability detection (SQL Injection, XSS, CSRF, auth issues, etc.)
- Performance analysis (inefficient algorithms, N+1 queries, memory leaks)
- Best practices enforcement (language-specific style guides, SOLID principles)
- Detailed issue reports with severity levels and fixes
- Pre-PR code quality gates

**Usage**: `/sanity-check-reviewer:sanity-check`

## Prerequisites

Before installing these plugins, ensure you have:

- **Claude Code CLI** - The official Claude Code command-line interface installed and configured
- **Git** - Version control system for cloning and managing the repository
- **Bash** - Unix shell (macOS/Linux native, Windows users need WSL or Git Bash)
- **Python 3.x** - Required for notification-hook plugin
- **pip** - Python package manager for installing dependencies

## Installation

1. Add the marketplace to your claude:
   ```bash
   /plugin marketplace add git@github.corp.ebay.com:Registration/claudePlugins.git
   ```

2. Install individual plugins to your Claude Code plugins directory:
   ```bash
   # Install the  plugin
   /plugin install <plugin-name>

   # Install the frontend-developer  plugin
   /plugin install frontend-developer
   ```

3. For MCP Launcher Wrapper plugin, additional configuration is required:
   ```bash
   cd ~/.claude/plugins/mcp-launcher-wrapper
   cp mcp-config.template.sh mcp-config.sh
   # Edit mcp-config.sh with your server paths and credentials
   ```

## Plugin Structure

Each plugin follows this structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── commands/
│   └── command-name.md      # Slash command definitions
├── scripts/                 # Optional scripts
└── README.md               # Plugin documentation
```


## Usage Examples

### Quick Start

After installing a plugin, you can use it directly in Claude Code:

```bash
# Use the frontend developer plugin to create a React component
/frontend-developer:frontend-developer

# Use the Java developer plugin for backend tasks
/java-developer:java-developer

# Run sanity check on your code before creating a PR
/sanity-check-reviewer:sanity-check

# Manage MCP servers
/mcp-launcher-manager
```

### Example: Creating a React Component

```bash
# In Claude Code, type:
/frontend-developer:frontend-developer

# Then describe what you need:
"Create a responsive navigation bar component with logo, menu items, and mobile hamburger menu"

# The plugin will generate a complete React component with TypeScript and Tailwind CSS
```

## Contributing

Contributions are welcome! To add a new plugin:

1. Fork the repository
2. Create your plugin following the structure above
3. Test thoroughly
4. Submit a pull request

Please ensure your plugin includes:
- A clear README.md with usage instructions
- Proper plugin.json manifest
- Well-documented command files
- Example usage scenarios

## Support

Need help or have questions?

- **Issues**: Report bugs or request features via [GitHub Issues](../../issues)
- **Discussions**: Ask questions and share ideas in [GitHub Discussions](../../discussions)
- **Documentation**: Check individual plugin README files for detailed documentation
- **Email**: Contact the maintainer at barnayak@ebay.com

## Authors and Acknowledgment

**Author**: Barsa Nayak

Special thanks to:
- The Claude Code team at Anthropic for creating the plugin system
- All contributors who have helped improve these plugins

## Project Status

**Status**: Active Development

This project is actively maintained and regularly updated with new plugins and improvements. Contributions and feedback are welcome!

## License

Copyright (c) 2025 Barsa Nayak

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
