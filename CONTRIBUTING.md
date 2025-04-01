# Contributing to My Frappe App

Thank you for considering contributing to my Frappe application! This document provides guidelines and instructions for contributing to this project.

## Setting Up Development Environment

### Prerequisites
- Python 3.7+
- Node.js 14+
- MariaDB/MySQL
- Git
- Frappe Bench

### Local Setup
1. Fork the repository
2. Clone your fork: 
   ```
   git clone https://github.com/your-username/block_administrator.git
   ```
3. Add upstream remote:
   ```
   git remote add upstream https://github.com/iamimmanuelraj/block_administrator.git
   ```
4. Create a new bench:
   ```
   bench init frappe-bench
   cd frappe-bench
   ```
5. Get the app:
   ```
   bench get-app block_administrator https://github.com/your-username/block_administrator.git
   ```
6. Install the app:
   ```
   bench --site site_name install-app block_administrator
   ```

## Coding Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use 4 spaces for indentation (no tabs)
- Use meaningful variable and function names
- Include docstrings for all functions, classes, and modules

### JavaScript
- Follow ESLint guidelines
- Use semicolons
- Use const/let instead of var
- Use clear and descriptive variable names

## Pull Request Process

1. Create a new branch for your feature or bugfix:
   ```
   git checkout -b feature-name
   ```
2. Make your changes and commit them with clear, descriptive messages
3. Push your branch to your fork:
   ```
   git push origin feature-name
   ```
4. Create a pull request against the upstream repository
5. Ensure your PR description clearly describes the problem and solution

## Commit Guidelines
- Use clear, descriptive commit messages
- Reference issue numbers in commit messages when applicable
- Keep commits focused on single changes when possible
- Format: `[type]: Short description (#issue)` where type can be feat, fix, docs, etc.

## Testing

Before submitting your PR, ensure:
1. All tests pass: `bench run-tests --app block_administrator`
2. For new features, add appropriate tests
3. For bug fixes, add tests that demonstrate the fix

## Documentation

- Update documentation for any changed functionality
- Document new features thoroughly
- Update README if necessary
- Use clear language and provide examples where appropriate

## Communication

- For issues or feature requests, use the GitHub Issues page
- Join the Frappe community forum for discussions

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [GNU General Public License v3.0](LICENSE).

Thank you for your contributions!
