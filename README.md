# Evelyn's Taekwondo Showdown

A web-based fighting game created for Evelyn's 8th birthday party, featuring taekwondo-inspired moves and animations.

## Game Overview

Evelyn's Taekwondo Showdown is a browser-based fighting game where players control a character to perform jumps, kicks, and punches against an AI opponent in a traditional dojo setting.

## Controls

### Desktop Controls:
- **Arrow Left/Right**: Move left/right
- **Arrow Up**: Jump
- **Spacebar**: Attack (alternates between kick and punch)

### Mobile Controls:
- **Left/Right Buttons**: Move left/right
- **Jump Button**: Jump
- **Attack Buttons**: Perform kicks and punches

## Required Files

### Image Assets
The game requires the following image files:

#### Character Sprites
- `evelyn-standing.png` - Default standing pose
- `evelyn-jump-001.png` - First jump animation frame
- `evelyn-jump-002.png` - Second jump animation frame
- `evelyn-kick-001.png` through `evelyn-kick-010.png` - Ten frames of kick animation

#### Background
- `dojo.jpg` - Dojo background image

### Audio Assets
The game uses the following audio file:
- `09. Ryu Stage.mp3` - Background music during gameplay

## Technical Details

### Technologies Used
- **Three.js** - For 3D rendering and animation
- **HTML5/CSS3** - For UI elements and styling
- **JavaScript** - For game logic and event handling

### Game Features
- Character movement and jumping physics
- Kick and punch attack animations
- Health bar system
- AI opponent with basic movement and attack patterns
- Mobile-friendly controls
- Background music during gameplay

## Installation and Running

1. Clone the repository
2. Ensure all image and audio files are in the root directory
3. Open `index.html` in a web browser
   - For best results, serve the files through a local web server (e.g., `python -m http.server`)

## Game States

The game has four main states:
1. **Loading** - Initial loading of assets
2. **Intro** - Title screen with start button
3. **Gameplay** - The main fighting sequence
4. **Ending** - Victory/defeat screen with play again option

## Development Notes

- The character uses sprite-based animations for jumps and kicks
- The game is designed to work on both desktop and mobile devices
- Audio playback requires user interaction due to browser policies
- The game uses a billboard technique to ensure characters always face the camera

## Credits

- Character sprites and background images created for Evelyn's Taekwondo Showdown
- Background music: "Ryu Stage Theme" from Street Fighter II
