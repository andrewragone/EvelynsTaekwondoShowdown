# System Patterns: Evelyn's Taekwondo Showdown

## System Architecture

*   **Initial Assessment:** The presence of `index.html`, `server.py`, and `requirements.txt` suggests a potential web-based architecture.
    *   `index.html`: Likely handles the frontend presentation (graphics, canvas).
    *   `server.py`: May serve the HTML/assets or handle game logic/state (less likely for a simple client-side game).
    *   `requirements.txt`: Indicates Python dependencies, reinforcing the use of a Python backend/server component.
*   **Alternative:** The game could be entirely client-side JavaScript within `index.html`, with `server.py` only used for local development serving. This needs verification.

## Key Technical Decisions (To Be Made)

*   **Game Engine/Library:** Will a specific JavaScript game library (e.g., Phaser, PixiJS) be used, or will it be built with vanilla JS and HTML Canvas?
*   **State Management:** How will player state (position, action, animation frame) be managed?
*   **Input Handling:** How will keyboard inputs be captured and translated into game actions?
*   **Animation:** How will sprite sequences be managed and rendered?

## Design Patterns (Potential)

*   **Game Loop:** A standard pattern for updating game state and rendering each frame.
*   **State Machine:** Could be used to manage Evelyn's states (idle, walking, jumping, kicking).
*   **Observer Pattern:** Potentially for handling events like input changes.

## Component Relationships (Initial View)

```mermaid
graph TD
    User[User Input] --> Client[Client (index.html/JS)]
    Client --> Render[Rendering (Canvas)]
    Client --> State[Game State Management]
    State --> Render
    Server[Server (server.py)] -- Serves --> Client
    Assets[Assets (.png, .jpg, .mp3)] --> Client

    subgraph Frontend
        Client
        Render
        State
        Assets
    end

    subgraph Backend (Potentially just for serving)
        Server
    end
```

*(This file outlines the technical structure and patterns, starting with observations from existing files.)*
