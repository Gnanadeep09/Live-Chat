# Python Chat App

Real-time chat application built with FastAPI, WebSockets, and SQLAlchemy.

## Professional Summary

A lightweight, high-performance real-time chat application utilizing event-driven WebSocket connections, localized SQLite persistence via SQLAlchemy ORM, and an asynchronous FastAPI backend framework.

## Core Features

* Real-Time Messaging: Implements persistent duplex communication channels via WebSockets.
* Data Persistence: Automated logging of history and dynamic lookup via SQLite and SQLAlchemy.
* Connection Lifecycle Management: Active tracking of connected clients with broad broadcast capabilities.

## Technical Stack

* Backend: Python, FastAPI, WebSockets
* Database & ORM: SQLite, SQLAlchemy 2.0+
* Frontend: HTML5, CSS3, Vanilla JavaScript

## Installation and Deployment

1. Install Dependencies
pip install -r requirements.txt
2. Initialize Database Models
python database.py
3. Launch Application Server
uvicorn main:app --reload

## System Architecture

* `database.py`: Handles connection pooling, thread routing configuration, and ORM declarations.
* `main.py`: Coordinates CORS handling, active connection manager classes, and stateful socket operations.
* `index.html`: Manages DOM injection, event tracking for text transmission, and structural layout.