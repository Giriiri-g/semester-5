// Initialize canvas and variables
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const tileSize = 10;
const mapWidth = 71;
const hudHeight = 60;

let isGameOver = false;
const hudColors = ["#F01FFF", "#D4A8FF", "#00EEFF", "#0011FF"];
const players = [
  { pos: [10, 9], icon: "@", hudIndex: 0 },
  { pos: [11, 30], icon: "#", hudIndex: 1 },
  { pos: [10, 58], icon: "$", hudIndex: 2 },
  { pos: [18, 27], icon: "&", hudIndex: 3 }
];
let hudValues = [
  { health: "♥♥♥♥♥", items: 0, score: 0 },
  { health: "♥♥♥♥♥", items: 0, score: 0 },
  { health: "♥♥♥♥♥", items: 0, score: 0 },
  { health: "♥♥♥♥♥", items: 0, score: 0 }
];
const bombList = [];
let gameMap, ogMap, hudNames;

// Map initialization
const rawMap = Map =  '       ╔══════════╗                                                   \n       ║∙∙∙∙∙∙∙∙∙∙║                               ╔══════════════════╗\n       ║∙∙∙∙∙∙∙∙∙∙║                               ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n       ╚══════╦═══╝                            ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n              ▒                         ▒▒▒▒▒▒▒▒  ╚╦═════════════════╝\n              ▒                         ▒          ▒                  \n        ▒▒▒▒▒▒▒                    ▒▒▒▒▒▒          ▒▒▒▒▒▒             \n╔═══════╩══════════╗               ▒              ╔═════╩════════════╗\n║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒            ▒              ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒  ╔═════════╩═╗            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║  ▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙∙∙∙∙∙∙∙∙║            ║∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙║\n╚═══════╦══════════╝     ╚═════════╦═╝            ╚══════════════════╝\n        ▒                   ▒▒▒▒▒▒▒▒                                  \n        ▒▒▒▒▒▒▒▒▒▒▒       ╔═╩═╗                                       \n       ╔══════════╩═╗    ▒╣∙∙∙║                          ╔════╗       \n       ║∙∙∙∙∙∙∙∙∙∙∙∙╠▒▒▒▒▒║∙∙∙║                          ║∙∙∙∙║       \n       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║                          ║∙∙∙∙║       \n       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙║  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣∙∙∙∙║       \n       ║∙∙∙∙∙∙∙∙∙∙∙∙║     ║∙∙∙╠▒▒▒                       ║∙∙∙∙║       \n       ╚════════════╝     ╚═══╝                          ╚════╝       \n';

function initGame(users = null) {
    gameMap = rawMap.split("\n");
    ogMap = rawMap.split("\n");
    hudNames = users || ["Giriirig", "PsylectrA", "Sukuna", "Puchandi"];
    renderMap();
    renderHUD();
}

// Map utilities
function getMapIndex([row, col]) {
    return row * mapWidth + col;
}

function isValidMove([row, col]) {
    const tile = gameMap[row][col];
    return !["║", "═", "╗", "╝", "╚", "╔", " "].includes(tile);
}

// Player actions
function movePlayer(playerIndex, direction) {
    const player = players[playerIndex];
    const newPos = [...player.pos];

    if (direction === "a") newPos[1] -= 1; // Left
    if (direction === "d") newPos[1] += 1; // Right
    if (direction === "w") newPos[0] -= 1; // Up
    if (direction === "s") newPos[0] += 1; // Down

    if (isValidMove(newPos)) {
        if (gameMap[newPos[0]][newPos[1]] === "!") {
            hudValues[player.hudIndex].items += 1;
            gameMap[newPos[0]][newPos[1]] = "∙";
        }
        player.pos = newPos;
        renderMap();
    }
}

// HUD rendering
function renderHUD() {
    ctx.fillStyle = "#A9A9A9";
    ctx.fillRect(0, 0, canvas.width, hudHeight);

    hudNames.forEach((name, i) => {
        const hud = hudValues[i];
        ctx.fillStyle = hud.health ? hudColors[i] : "red";
        ctx.fillText(
            `${name}: ${hud.health} ☼x${hud.items} ɸx${hud.score}`,
            10 + i * 300,
            30
        );
    });
}

// Map rendering
function renderMap() {
    // Clear the canvas below the HUD
    ctx.clearRect(0, hudHeight, canvas.width, canvas.height);

    // Render each row and column of the map starting below the HUD
    gameMap.forEach((row, rowIndex) => {
        row.split("").forEach((tile, colIndex) => {
            const x = colIndex * tileSize;
            const y = hudHeight + rowIndex * tileSize;

            ctx.fillStyle = getTileColor(tile);
            ctx.fillText(tile, x, y);
        });
    });

    // Render players on top of the map
    players.forEach((player) => {
        const [row, col] = player.pos;
        const x = col * tileSize;
        const y = hudHeight + row * tileSize;

        ctx.fillStyle = hudColors[player.hudIndex];
        ctx.fillText(player.icon, x, y);
    });
}


function getTileColor(tile) {
    switch (tile) {
        case "║":
        case "═":
        case "╗":
        case "╝":
        case "╚":
        case "╔":
        case "╦":
        case "╩":
        case "╠":
        case "╬":
            return "#AA5500"; // Walls and doorways
        case "∙":
            return "#50F050"; // Movable space
        case "!":
            return "#FBFB54"; // Item
        case "▒":
            return "#A7A7A7"; // Passage
        case " ":
            return "black"; // Empty space
        default:
            return "grey"; // Undefined tiles
    }
}



// Bomb handling
function placeBomb(playerIndex) {
    const player = players[playerIndex];
    bombList.push({ pos: [...player.pos], timer: 60, playerIndex });
    hudValues[player.hudIndex].items -= 1;
    gameMap[player.pos[0]][player.pos[1]] = "☼";
    renderMap();
}

function detonateBomb(bombIndex) {
    const bomb = bombList[bombIndex];
    gameMap[bomb.pos[0]][bomb.pos[1]] = ogMap[bomb.pos[0]][bomb.pos[1]];
    bombList.splice(bombIndex, 1);
    renderMap();
}

// Game loop
function gameLoop() {
    if (isGameOver) return;

    bombList.forEach((bomb, index) => {
        bomb.timer -= 1;
        if (bomb.timer <= 0) detonateBomb(index);
    });

    renderHUD();
    requestAnimationFrame(gameLoop);
}

// Event listener
document.addEventListener("keydown", (e) => {
    switch (e.key) {
        case "ArrowLeft":
        case "a":
            movePlayer(0, "a");
            break;
        case "ArrowRight":
        case "d":
            movePlayer(0, "d");
            break;
        case "ArrowUp":
        case "w":
            movePlayer(0, "w");
            break;
        case "ArrowDown":
        case "s":
            movePlayer(0, "s");
            break;
        case " ":
            placeBomb(0);
            break;
    }
});

// Start game
initGame();
gameLoop();
