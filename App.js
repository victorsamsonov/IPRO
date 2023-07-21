import { useState } from "react";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";
import LOGO from "./maze-puzzle-strategy-business-plan-2-8688.png";
import FOOTER from "./illinois-tech-with-seal.png";

function App() {
  // new line start
  const [profileData, setProfileData] = useState(null);
  const [classSelected, setClassSelected] = useState("Select Class");
  const [gpa, setGPA] = useState("3.6");
  const [error, setError] = useState("");
  const [predction, setPrediction] = useState(null);
  const CLASS_OPTIONS = [
    "CS 100",
    "CS 116",
    "CS 350",
    "CS 450",
    "CS 351",
    "CS 340",
    "CS 440",
    "CS 430",
    "CS 485",
    "CS 487",
    "CS 484",
    "CS 422",
    "MATH 151",
    "MATH 152",
    "MATH 251",
    "MATH 322",
    "MATH 252",
    "CS 331",
    "CS 330",
    "MATH 474",
    "ELECT 1",
    "ELECT 2",
    "ELECT 3",
  ];

  const handleSelectChange = (event) => {
    setClassSelected(event.target.value);
    console.log(event.target.value);
  };

  const Options = () => {
    return (
      <div className="custom-select ">
        <select
          onChange={handleSelectChange}
          id="class-options"
          // disabled={classSelected !== ""}
        >
          <option value="">{classSelected}</option>
          {CLASS_OPTIONS.map((option) => (
            <option value={option}>{option}</option>
          ))}
        </select>
      </div>
    );
  };

  const OptionsHardCodedSemester = () => {
    return (
      <div className="custom-select ">
        <select
          id="class-options"
          // disabled={classSelected !== ""}
        >
          <option value="Fall 2023">{`Fall 2023`}</option>
        </select>
      </div>
    );
  };

  const OptionsHardCodedProfessor = () => {
    return (
      <div className="custom-select ">
        <select
          id="class-options"
          // disabled={classSelected !== ""}
        >
          <option value="Professor 1">{`Professor ${1}`}</option>
          {CLASS_OPTIONS.map((option, index) => (
            <option value={`Professor ${index}`}>{`Professor ${index+2}`}</option>
          ))}
        </select>
      </div>
    );
  };

  const handleGPAChange = (event) => {
    setGPA(event.target.value);
    setError("");
  };

  const handleSubmitGPA = (event) => {
    event.preventDefault();
    if (isValidGPA(gpa)) {
      // Do something with the valid GPA value
      console.log("Submitted GPA:", gpa);
    } else {
      setGPA("");
      setError("Please enter a valid GPA between 0 and 4.");
    }
  };

  const isValidGPA = (value) => {
    const parsedValue = parseFloat(value);
    return !isNaN(parsedValue) && parsedValue >= 0 && parsedValue <= 4;
  };

  const GPAInput = () => {
    return (
      <form onSubmit={handleSubmitGPA}>
        <label>
          GPA:
          <input
            type="text"
            value={gpa}
            onChange={(e) => setGPA(e.target.value)}
            placeholder="enter gpa"
          />
        </label>
      </form>
    );
  };

  function predict() {
    console.log("axios");
    axios
      .post("/predict", { gpa: gpa, class: classSelected })
      .then((response) => {
        console.log(response);
        let currPrediction = response.data.processed_pred;
        console.log(currPrediction);
        setPrediction(currPrediction);
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }
  //end of new line

  return (
    <div className="App">
      <div className="title-wrapper">
        <h1>GRADPATH AI </h1>
        <img src={LOGO} className="gradpath-logo" />
      </div>
      <h2>Demo</h2>

      <div className="App-header">
        <div className="about-container">
          <text>
            Select the Class that Interests you and provide your current GPA:
          </text>
        </div>
        <div>
          <text>Username: John Doe</text>
          <text>Major: Computer Engineering</text>
        </div>
        <div className="options-container">
          <GPAInput />
          <OptionsHardCodedSemester/>
          <OptionsHardCodedProfessor/>
          <Options />
          <button
            children="disabled at 10 chars"
            disabled={gpa.length >= 4}
            onClick={predict}
            type="submit"
          >
            Submit
          </button>
        </div>
        <h3 className="section-text">Predictions:</h3>
        {predction && (
          <div className="outputs-container">
            <text className="prediction-text">
              {"  "}If you decide to take <b> {classSelected}</b> in Fall 2023,
              given your GPA of <b>{gpa}</b> and past student performance, we
              predict your grade will be: <b>{predction}</b>{" "}
            </text>
          </div>
        )}
      </div>
      <footer>
        <img src={FOOTER} className="footer-img" />
      </footer>
    </div>
  );
}

export default App;
