import React from 'react';
// import {guest1} from '../Images/img1.jpg';
import img from '../Images/bg3.jpg';

// import {logo} from '../Images/logo.jpg';

function LandingPage() {
  return (
<>
 
    <div className="bg-cover bg-center h-screen w-full"
            style={{backgroundImage: `url(${img})`}} >
     

      <header className="container mx-auto px-4 py-8 flex justify-between items-center">
        <nav>
          <ul className="flex space-x-4">
            {/* <li>
              <a href="signin" className="text-3xl hover:bg-red-800 bg-black text-white border-4 rounded-xl px-3 ">SignIn</a>
            </li> */}
          </ul>
        </nav>
      </header>
      <div>
      <main className="container mx-auto px-4 py-16 flex flex-col items-center space-y-8 mt-10">
        <h2 className="text-7xl font-bold text-black mt-12">We Build Amazing</h2>
        <p className=" text-black text-lg mt-12">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.<br></br>
          consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
     
        <a href="SignIn" className=" bg-white hover:bg-orange-400 text-black font-bold py-2 px-4 rounded mt-16">
          GET STARTED
        </a>
      </main>
    </div>
    </div>
    </>
  );
}

export default LandingPage;
