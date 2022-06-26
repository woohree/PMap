import React from 'react'
import { BrowserRouter, Route, Routes, NavLink } from 'react-router-dom'
import Home from './pages/Home/Home'
import NotFound from './pages/NotFound/NotFound'
import Location from './pages/Home/Location'


function App() {
  return (
    <BrowserRouter>
      <div>
        <h1>MAIN</h1>
        <ul>
          <li><NavLink to="/">HOME</NavLink></li>
          <li><NavLink to="/location">MAP</NavLink></li>
        </ul>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/location" element={<Location/>}></Route>
          <Route path="*" element={<NotFound/>}></Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
