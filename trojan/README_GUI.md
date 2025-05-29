# 🛡️ System Security & Optimization Tool

A modern GUI-based system maintenance tool with a clean, professional interface.

## Features

### 🔍 Virus Scanner
- Scans for suspicious files in the current directory
- Shows detected files in an organized list
- One-click removal of suspicious files
- Real-time scan results

### 🚀 System Speed Optimizer
- Optimize system performance by creating file backups
- Select any file to optimize
- Configurable number of optimization copies (1-100)
- Progress tracking during optimization
- Automatic file refresh

### 🔧 Problem Fixer
- Fix corrupted or problematic files
- Secure files by applying system-level hiding
- Browse and select files from current directory
- Cross-platform compatibility (Windows/Linux/macOS)

### 📋 Activity Log
- View all system operations
- Timestamped activity records
- Scrollable log viewer
- Session tracking

## Installation

No installation required! Just run:

```bash
python3 system_tool.py
```

## Requirements

- Python 3.6+
- tkinter (usually included with Python)
- Standard library modules: `os`, `platform`, `datetime`, `shutil`, `glob`, `pathlib`, `threading`

## Usage

1. **Launch the tool**: `python3 system_tool.py`
2. **Select a function**: Click any of the main buttons
3. **Follow the interface**: Each function opens in its own window
4. **Monitor activity**: Use the log viewer to track operations

## Interface

- **Modern dark theme** for professional appearance
- **Intuitive button layout** with clear icons
- **Separate windows** for each function
- **Real-time progress tracking**
- **User-friendly error handling**

## Security Features

- **Activity logging** for all operations
- **Confirmation dialogs** for destructive actions
- **Error handling** to prevent crashes
- **Cross-platform file operations**

## File Operations

- **Virus Scanner**: Targets .txt files for removal
- **Speed Optimizer**: Creates numbered copies with "_optimized" suffix
- **Problem Fixer**: Renames files with ".fixed" extension and applies OS-specific hiding

---

*Professional system maintenance tool with modern GUI interface* 