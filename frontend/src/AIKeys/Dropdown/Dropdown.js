import React, { useState , useRef} from "react";
import './Dropdown.css';
import {useDetectOutsideClick} from "./useDetectOutsideClick.js"

function DropdownMenu(props) {
    const dropdownRef = useRef(null);
    const [isActive, setIsActive] = useDetectOutsideClick(dropdownRef, false);
    const [currentLabel, setLabel] = useState("python");
    const onClick = () => setIsActive(!isActive);


    const reactToDropdownClick = (label) => {
        setIsActive(!isActive);
        setLabel(label);
        props.onClickButton(label)
      };
  
    return (
        <div className="menu-container">
        <button onClick={onClick} className="menu-trigger">
          <span>{currentLabel}</span>
        </button>
        <nav ref={dropdownRef} className={`menu ${isActive ? 'active' : 'inactive'}`}>
            <ul>
                <li><p onClick={() => reactToDropdownClick("python")}>python</p></li>
                <li><p onClick={() => reactToDropdownClick("swift")}>swift</p></li>
            </ul>
        </nav>
      </div>
    );
  };

  export default DropdownMenu;

  // <li><p onClick={() => reactToDropdownClick("swift")}>swift</p></li>