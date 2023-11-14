import './App.css';

// Array of reuit names:

let someFruit = [
  "mangoes",
  "pear",
  "oranges",
  "strawberries",
  "bananas"
]

function App() {
  return (
    <div className="App">
      <h1>The Fruit App!</h1>
      <ul>
        {
          someFruit.map((fruit => {
            return <li>{fruit}</li>
          }))
        }
      </ul>
    </div>
  );
}

export default App;
