# Web Archive
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![newspaper](https://img.shields.io/badge/library-newspaper-blue)
![beautifulsoup](https://img.shields.io/badge/library-beautifulsoup-blue)
![License](https://img.shields.io/github/license/cadencejames/web-archive)
![Last Commit](https://img.shields.io/github/last-commit/cadencejames/web-archive)
![Contributors](https://img.shields.io/github/contributors/cadencejames/web-archive)
[![Network Tool](https://img.shields.io/badge/network-tool-green)](https://github.com/cadencejames/web-archive)

A **simple and crude archiver** for webpages and images.

This tool allows users to save a copy of web content, including HTML pages and associated images, for offline storage and reference.

---

## Features
- Downloads and saves HTML content of a webpage.
- Archives images linked from the webpage.
- Stores archived content in a structured folder system for easy access.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/cadencejames/web-archive.git
   ```

2. Navigate to the project directory:
   ```bash
   cd web-archive
   ```
   
3. Install the required dependencies (if any are listed in `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```


---

## Usage

1. Run the main script:
   ```bash
   python web_archiver.py
   ```

2. Provide the URL of the webpage to archive when prompted.

3. View the saved HTML and images in the `archive` folder.

---

## Folder Structure
```
web-archive/
├── archive/
│   ├── [timestamp]/
│   │   ├── index.html      # Saved webpage
│   │   ├── images/         # Folder containing downloaded images
├── web_archiver.py         # Main script
```

---

## Contributing

Contributions are  welcome! If you have ideas or fixes, feel free to:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---