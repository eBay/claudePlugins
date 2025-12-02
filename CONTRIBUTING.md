# Contributing to claudePlugins

Thank you for your interest in contributing to claudePlugins! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Issues

- Use the issue tracker to report bugs or suggest features
- Check if the issue already exists before creating a new one
- Provide detailed information including steps to reproduce bugs
- Include relevant environment details (OS, Claude Code version, etc.)

### Submitting Changes

1. **Fork the Repository**
   - Fork the project to your GitHub account
   - Clone your fork locally

2. **Create a Branch**
   - Create a feature branch from `main`
   - Use descriptive branch names (e.g., `feature/new-plugin`, `fix/issue-123`)

3. **Make Your Changes**
   - Follow the existing code style and conventions
   - Write clear, concise commit messages
   - Test your changes thoroughly
   - Update documentation as needed

4. **Test Your Plugin**
   - Ensure your plugin works with Claude Code
   - Verify all features function as expected
   - Check for any breaking changes

5. **Submit a Pull Request**
   - Push your changes to your fork
   - Create a pull request to the main repository
   - Provide a clear description of your changes
   - Reference any related issues

## Plugin Development Guidelines

### Plugin Structure

Each plugin should follow this structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (required)
├── commands/
│   └── command-name.md      # Slash command definitions
├── scripts/                 # Optional scripts
├── hooks/                   # Optional hooks
└── README.md               # Plugin documentation (required)
```

### Plugin Manifest (plugin.json)

Your plugin must include a valid `.claude-plugin/plugin.json` file:

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Brief description of your plugin",
  "author": "Your Name"
}
```

### Documentation Requirements

- Each plugin must have a README.md with:
  - Clear description of what the plugin does
  - Installation instructions
  - Usage examples
  - Configuration details (if applicable)
  - Any dependencies or prerequisites

### Code Quality

- Write clean, maintainable code
- Include comments for complex logic
- Follow language-specific best practices
- Ensure cross-platform compatibility when possible

### Testing

- Test your plugin with Claude Code before submitting
- Include test files or test instructions
- Document any known limitations

## Adding a New Plugin

To contribute a new plugin:

1. Create a new directory under `plugins/` with your plugin name
2. Follow the plugin structure outlined above
3. Create your plugin manifest and documentation
4. Implement your plugin functionality
5. Test thoroughly
6. Submit a pull request

## Code Review Process

- All contributions will be reviewed by maintainers
- Feedback may be provided for improvements
- Changes may be requested before merging
- Be responsive to comments and questions

## Code of Conduct

- Be respectful and professional
- Welcome newcomers and help others learn
- Focus on constructive feedback
- Maintain a positive environment

## Getting Help

If you need help with your contribution:

- Check existing documentation and examples
- Review other plugins for reference
- Ask questions in pull request comments
- Reach out to maintainers if needed

## License and Copyright

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.

### Copyright Headers

All source code files (Python, JavaScript, Shell scripts, etc.) must include the following copyright header at the top:

**For Python files (.py):**
```python
# Copyright 2025 Barsa Nayak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

**For Shell scripts (.sh):**
```bash
#!/bin/bash
# Copyright 2025 Barsa Nayak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

**For JavaScript files (.js):**
```javascript
/**
 * Copyright 2025 Barsa Nayak
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
```

### Contributor Agreement

When you submit a pull request, you are agreeing to the following:

1. You certify that you have the right to submit the contribution under the Apache License 2.0
2. You grant the project maintainers a perpetual, worldwide, non-exclusive, no-charge, royalty-free license to use, reproduce, modify, and distribute your contributions
3. Your contributions are provided "as-is" without warranties of any kind
4. You understand that your contributions may be redistributed under the Apache License 2.0

### File Modifications

When modifying existing files:
- Keep the original copyright header intact
- Add your copyright notice if making substantial changes
- Update the year if applicable

Example:
```python
# Copyright 2025 Barsa Nayak
# Copyright 2025 Your Name (if making substantial modifications)
#
# Licensed under the Apache License, Version 2.0...
```

Thank you for contributing to claudePlugins!
