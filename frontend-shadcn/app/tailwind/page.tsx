import { Button } from "@/components/ui/button";
import React from "react";

const TailwindPage = () => {
  return (
    <div className="bg-gray-100 p-4 rounded-lg flex item-center justify-center">
        <div className="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5">
            <img src="../avatar.png" className="size-12 shrink-0"/>
            <div>
                <div className="text-xl font-medium text-black">Hyung</div>
                <p className="text-gray-500">You have a new message!</p>
            </div>
        </div>
      {/* <div className="bg-white mt-2 text-gray-600">
        <div>This is contents.</div>
        <div>
          <button className="pl-6 pr-6 pt-2 pb-2 rounded-xl text-white text-lg border-white border-lg bg-sky-500 hover:bg-sky-700 focus:outline-2 focus:outline-violet-700">
            Hello
          </button>
        </div>
      </div> */}
    </div>
  );
};

export default TailwindPage;
