# Mutimedia-compression-based-digital-library
Python-based Multimedia Compression Digital Library System for uploading, managing, and compressing images, audio, videos, and PDFs. Built with Tkinter GUI and ZIP DEFLATE compression to optimize storage. The system stores compressed files and displays original and compressed sizes for easy comparison.
# Multimedia Compression-Based Digital Library System

A Python-based desktop application that combines **multimedia file management** with **lossless compression**. The system allows users to upload images, audio, videos, and PDF files through a simple Tkinter GUI. Uploaded files are automatically compressed using **ZIP with DEFLATE compression** and stored for efficient file management.

## 📌 Project Overview

The Multimedia Compression-Based Digital Library System is designed to provide a simple digital repository for multimedia resources while applying compression techniques to optimize storage.

The system provides a graphical interface where users can:

- Upload multimedia files
- Store uploaded files in an organized folder
- Automatically compress files
- Store compressed files separately
- View original and compressed file sizes
- Manage different types of digital resources

## 🎯 Objectives

- To develop a simple digital multimedia library.
- To implement lossless file compression.
- To reduce storage requirements where compression is effective.
- To provide an easy-to-use graphical interface.
- To compare original and compressed file sizes.
- To organize multimedia resources systematically.

## ✨ Features

- 🖼️ Image file support
- 🎵 Audio file support
- 🎥 Video file support
- 📄 PDF file support
- 🗜️ ZIP/DEFLATE compression
- 🖥️ Tkinter graphical user interface
- 📊 Original vs. compressed size comparison
- 📁 Separate storage for uploaded and compressed files
- 🔄 Automatic compression after upload

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical User Interface |
| `zipfile` | ZIP compression |
| DEFLATE | Lossless compression algorithm |
| `os` | File and folder management |
| `shutil` | File copying and handling |

## 🧩 System Architecture

```text
              ┌───────────────┐
              │     User      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  Tkinter GUI  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  File Upload  │
              │    Module     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  Compression  │
              │    Module     │
              │ ZIP + DEFLATE │
              └───────┬───────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
      ┌──────────────┐  ┌───────────────┐
      │   Uploaded   │  │   Compressed  │
      │    Files     │  │     Files     │
      └──────────────┘  └───────┬───────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Digital Library │
                       │     Viewer      │
                       └─────────────────┘
