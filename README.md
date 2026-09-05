# ComfyUI-GooglePusher

A lightweight, dependency-free custom node for ComfyUI that pushes formatted text outputs directly to a Google Apps Script Web App endpoint to update Google Docs in real time.

Built to bypass bloated third-party HTTP request nodes that introduce unnecessary audio/video dependencies, using native Python standard libraries (`urllib` and `json`).

---

## Features

* **Zero External Dependencies:** Runs entirely on native Python packages without breaking desktop environments.
* **Dynamic Content Injection:** Streams text directly from LLM nodes (e.g., Gemini, Ollama) into cloud documents.
* **Real-Time Return:** Captures and outputs the live Google Docs URL directly inside the ComfyUI interface.

---

## Installation

1. Navigate to your ComfyUI custom nodes directory: `cd ComfyUI/custom_nodes`
2. Clone this repository: `git clone https://github.com/harsh-shrivas/ComfyUI-GooglePusher.git`
3. Restart ComfyUI. (Zero external packages required).

---

## Usage

* **Category:** `Custom/Pipeline`
* **Node Name:** `Google Pusher`
* Paste your Google Apps Script Web App deployment URL into the configuration field.
* Route any generated text string into the node's input pin and click **Queue Prompt** to execute and sync live to your cloud document.
