import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './components/Homepage';
import SignInPage from './components/SignInPage';
import Landing from './components/Landing';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/home" element={<HomePage />} />
                <Route path="/signin" element={<SignInPage />} />
                <Route path="/" element={<Landing/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
