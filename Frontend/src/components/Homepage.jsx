import React, { useState } from "react";
import { BsChevronCompactLeft, BsChevronCompactRight } from 'react-icons/bs';
import { RxDotFilled } from 'react-icons/rx';

import guest2 from "../Images/img1.jpg";
import guest1 from "../Images/img2.0.jpg";
import guest3 from "../Images/img3.jpg";
import tshirt1 from "../Images/img4.jpg";
import tshirt2 from "../Images/img5.jpg";
import tshirt3 from "../Images/img6.jpg";
import watches1 from "../Images/img7.jpg";
import watches2 from "../Images/img8.0.jpg";
import watches3 from "../Images/img9.jpg";

const Home = () => {
    const slides = [
        {
            url: watches2
        },
        {
            url: tshirt1
        },
        {
            url: guest3
        },
        {
            url: tshirt3
        },
        {
            url: guest2
        },
    ];

    const [currentIndex, setCurrentIndex] = useState(0);

    const prevSlide = () => {
        const isFirstSlide = currentIndex === 0;
        const newIndex = isFirstSlide ? slides.length - 1 : currentIndex - 1;
        setCurrentIndex(newIndex);
    };

    const nextSlide = () => {
        const isLastSlide = currentIndex === slides.length - 1;
        const newIndex = isLastSlide ? 0 : currentIndex + 1;
        setCurrentIndex(newIndex);
    };

    const goToSlide = (slideIndex) => {
        setCurrentIndex(slideIndex);
    };

    const Card = ({ img, name }) => {
        return (
            <>

                <div className="flex flex-row items-center justify-center w-[80vw] md:w-[60vw] h-full lg:w-1/2 my-10 p-5 bg-mentor-card rounded-xl shadow-[0_0_10px_1px_rgba(0,0,0)]">
                    <img src={img} alt="KG" className="w-[180px] h-[220px] rounded-lg " />
                    <div>
                        <button className=" text-xl font-bold cursor-pointer rounded-2xl w-16 bg-stone-600 text-white hover:bg-orange-500 py-3 ">{name}</button>
                    </div>
                </div>
            </>
        );
    };

    const cards = () => {
        const guests = [
            { id: 1, img: guest1, name: "Try It" },
            { id: 2, img: guest2, name: "Try It" },
            { id: 3, img: guest3, name: "Try It" },
        ];

        const tshirt = [
            { id: 1, img: tshirt1, name: "Try It" },
            { id: 2, img: tshirt2, name: "Try It" },
            { id: 3, img: tshirt3, name: "Try It" },
        ];

        const watches = [
            { id: 1, img: watches1, name: "Try It" },
            { id: 2, img: watches2, name: "Try It" },
            { id: 3, img: watches3, name: "Try It" },
        ];

        return (

            <div>
        <span className="flex justify-center border rounded-lg text-shadow my-10 text-4xl font-medium mt-0 py-6 bg-black text-white font-serif">
          Eyewear Collection
        </span>
                <div className="w-[90%] gap-16 ml-16 flex flex-row items-center justify-center h-auto">

                    {guests.map(({ id, img, name }) => (
                        <Card key={id} img={img} name={name} />

                    ))}
                </div>

                <span className="flex justify-center border rounded-lg text-shadow my-10 text-4xl font-medium mt-0 py-6 bg-black text-white font-serif">
          Clothing Collection
        </span>
                <div className="w-[90%] gap-16 ml-16 flex flex-row items-center justify-center h-auto">
                    {tshirt.map(({ id, img, name }) => (
                        <Card key={id} img={img} name={name} />
                    ))}
                </div>

                <span className="flex justify-center border rounded-lg text-shadow my-10 text-4xl font-medium mt-0 py-6 bg-black text-white font-serif">
          Wristwatch Collection
        </span>
                <div className="w-[90%] gap-16 ml-16 flex flex-row items-center justify-center h-auto">
                    {watches.map(({ id, img, name }) => (
                        <Card key={id} img={img} name={name} />
                    ))}
                </div>
            </div>
        );
    };

    return (
        <>
            <div>
                {/* <FaMagnificationGlass/> */}
                <input
                    type="text"
                    placeholder="Search for any student data"
                    className="py-2 w-1/2 mt-2 text-center font-normal text-sm border border-gray-400 rounded-full focus:outline-none focus:ring focus:ring-blue-200 ml-20 "
                />
            </div>
            <div className="max-w-[1130px] h-[610px] w-full m-auto py-16 px-4 relative group">
                <div
                    style={{ backgroundImage: `url(${slides[currentIndex].url})` }}
                    className="w-full h-full rounded-2xl bg-center bg-cover duration-500"
                ></div>
                {/* Left Arrow */}
                <div className="hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] left-5 text-2xl rounded-full p-2 bg-black/20 text-white cursor-pointer">
                    <BsChevronCompactLeft onClick={prevSlide} size={30} />
                </div>
                {/* Right Arrow */}
                <div className="hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] right-5 text-2xl rounded-full p-2 bg-black/20 text-white cursor-pointer">
                    <BsChevronCompactRight onClick={nextSlide} size={30} />
                </div>
                <div className="flex top-4 justify-center py-2">
                    {slides.map((slide, slideIndex) => (
                        <div
                            key={slideIndex}
                            onClick={() => goToSlide(slideIndex)}
                            className="text-2xl cursor-pointer"
                        >
                            <RxDotFilled />
                        </div>
                    ))}
                </div>

                {cards()} {/* Calling the cards function */}
            </div>
        </>
    );
};

export default Home;