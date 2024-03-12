import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
// import {bg} from '../Images/bg2.png';

const SignIn = () => {
    const [username, setUsername] = useState('');
    const [email, setemail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const navigate = useNavigate();

    const handleSignIn = (e) => {
        e.preventDefault();

        setErrorMessage(''); // Clear any existing errors initially

        // Basic Validation
        if (username.length < 5 || password.length < 8) {
            setErrorMessage('Username must be at least 5 characters, password at least 8 characters');
            return;
        }

        // Redirect to Homepage
        navigate('/home');
    };

    return (
        <>
         {/* <div className="bg-cover bg-center h-full w-full"
            style={{backgroundImage: `url(${bg})`}} ></div> */}
            <form onSubmit={handleSignIn}>
                <div className="flex flex-col md:flex-row justify-center items-center bg-gradient-to-r from-[#00050B] to-[#4E5C6C] h-screen">
                    {/* Space for Image (if desired) ... */}

                    {/* Login Form */}
                    <div className="w-full md:w-2/5 p-10 justify-center items-center">
                        <div className="bg-white p-8 shadow-md rounded-lg">
                            <h2 className="flex justify-center text-2xl font-semibold">Sign Up</h2>

                            {errorMessage && <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                                {errorMessage}
                            </div>}

                            <div className="mb-4">
                                <label htmlFor="username" className="block text-sm font-medium text-gray-600">
                                    Username
                                </label>
                                <input
                                    type="text"
                                    id="username"
                                    name="username"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    className="mt-1 p-2 w-full border rounded-md"
                                    required
                                />
                            </div>

                            <div className="mb-4">
                                <label htmlFor="email" className="block text-sm font-medium text-gray-600">
                                    Email Address
                                </label>
                                <input
                                    type="email"
                                    id="email"
                                    name="email"
                                    value={email}
                                    onChange={(e) => setemail(e.target.value)}
                                    className="mt-1 p-2 w-full border rounded-md"
                                    required
                                />
                            </div>

                            <div className="mb-4">
                                <label htmlFor="password" className="block text-sm font-medium text-gray-600">
                                    Create Password
                                </label>
                                <input
                                    type="password"
                                    id="password"
                                    name="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="mt-1 p-2 w-full border rounded-md"
                                    required
                                />
                            </div>

                            <div className="text-right flex justify-center mt-6">
                                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                                    Sign Up
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </>
    );
};

export default SignIn;
