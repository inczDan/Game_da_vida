<template>
  <div id="GridCp">
      <h1 class="h1">Joguin da vida</h1>
          <div
          class="grid"
          :style="{
              'grid-template-columns': `repeat(${SIZE}, 17px)`,
              'grid-template-rows': `repeat(${SIZE}, 17px)`,
              }">
          <div
              v-for="(row, rowIndex) in grid"
              :key="`row-${rowIndex}`"
              class="row">
              <div
              v-for="(cell, collIndex) in row"
              :key="`cell-${collIndex}`"
              class="cell"
              :style="{
                  'background-color': grid[rowIndex][collIndex]
                  ? 'rgb(10, 10, 80)'
                  : 'rgb(90, 108, 190)'
              }"
              @mousedown="toggleCell(rowIndex, collIndex)">
              </div>
          </div>
      </div>
      <div class="buttons">
          <button
          :class="running ? 'stop' : 'start'"
          :disabled="!ready"
          @click="alternador()">
          {{ running ? 'Parar' : 'Iniciar'}}
          </button>
      </div>
  </div>
</template>

<script>
export default {
name: 'GridCp',
data () {
  return {
    running: false,
    grid: [],
    COLS: 40,
    ROWS: 40,
    // vizinhos
    vizinhas: [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ],
    SPEED: 180,
    SIZE: 40,
    ready: false,
    generation: 0
  }
},
mounted () {
  this.seedGrid()
},
methods: {
  cellViva () {
    for (let i = 0; i < this.grid.length; i++) {
      const row = this.grid[i]
      if (row.some(col => col)) {
        this.ready = true
        break
      } else {
        this.ready = false
      }
    }
  },
  alternador () {
    if (this.grid.length && this.ready) {
      this.running = !this.running
      this.simula()
    }
  },
  updateSize () {
    this.COLS = this.SIZE
    this.ROWS = this.SIZE
    this.seedGrid()
  },
  simula () {
    if (this.running) {
      const newGrid = this.grid.map(row => [...row])

      for (let row = 0; row < this.ROWS; row++) {
        for (let col = 0; col < this.COLS; col++) {
          let neighbours = 0

          for (let k = 0; k < this.vizinhas.length; k++) {
            const [x, y] = this.vizinhas[k]
            const newRow = row + x
            const newCol = col + y

            if (newRow >= 0 && newRow < this.ROWS && newCol >= 0 && newCol < this.COLS) {
              neighbours += this.grid[newRow][newCol]
            }
          }

          if (neighbours < 2 || neighbours > 3) {
            newGrid[row][col] = 0
          } else if (!this.grid[row][col] && neighbours === 3) {
            newGrid[row][col] = 1
          }
        }
      }

      this.grid = newGrid
      this.generation += 1

      setTimeout(this.simula, this.SPEED)
    }
  },
  gridVazio () {
    this.ready = false

    if (!this.running) {
      this.generation = 0
      this.grid = this.geraGrid(false)
    }
  },
  toggleCell (row, col) {
    if (!this.running) {
      const newGrid = [...this.grid]
      newGrid[row][col] = this.grid[row][col] ? 0 : 1
      this.grid = newGrid
    }

    this.cellViva()
  },
  nmRandom () {
    return Math.floor(Math.random() * 2)
  },
  geraGrid (fill = false) {
    const grid = []

    for (let row = 0; row < this.ROWS; row++) {
      grid[row] = []
      for (let col = 0; col < this.COLS; col++) {
        grid[row][col] = fill ? this.nmRandom() : 0
      }
    }

    return grid
  },
  seedGrid () {
    if (!this.running) {
      this.generation = 0
      this.grid = this.geraGrid()
      this.ready = true
    }
  }
}
}
</script>

<style>
html, body {
margin: 0;
height: 100%;
background: rgb(141, 139, 210);
background: linear-gradient(159deg, rgba(2,0,36,1) 0%, rgba(9,118,121,1) 44%, rgba(0,212,255,1) 100%);
font-size: 24px;
font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

#app {
height: 100%;
display: flex;
flex-direction: column;
align-items: center;
}

h1 {
color: rgb(141, 139, 210);
margin: 0.5rem;
text-align: center
}

.grid {
display: grid;
margin-bottom: 0.5rem;
margin-left: 27.5%;
}

.buttons {
display: flex;
justify-content: space-around;
}

button {
margin: 1rem;
cursor: pointer;
padding: 0.5rem;
border-radius: 4px;
border-style: none;
box-shadow: rgba(0, 0, 0, 0.25) 0px 3px 8px;
background-color: rgb(232, 178, 221);
}

button:hover, button:focus, button:active {
box-shadow: rgba(0, 0, 0, 0.50) 0px 3px 8px;
position: relative;
bottom: 2px;
}

.start {
width: 4rem;
background-color: rgb(151, 252, 159);
font-weight: bold;
}

.stop {
width: 4rem;
background-color: rgb(199, 60, 60);
font-weight: bold;
color: white;
}
.collrows {
grid-template-columns: repeat(40, 24px);
grid-template-rows: repeat(40, 16px);
}
.cell {
width: 100%;
height: 100%;
background-color: rgb(195, 167, 167);
cursor: pointer;
}
</style>
