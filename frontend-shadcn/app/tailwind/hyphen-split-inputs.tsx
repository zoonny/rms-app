"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import React, { useState } from "react";

const initialState = {
  text1: "",
  text2: "",
  text3: "",
  text4: "",
  text5: "",
};

function HyphenSplitInputs() {
  const [formData, setFormData] = useState(initialState);
  const [invalidPastedFormat, setInvalidPasteFormat] = useState(false);

  // 붙여넣기 이벤트 처리 함수: 클립보드에서 문자열을 읽어와서 하이픈(-) 기준으로 분리
  const handlePaste = (e) => {
    e.preventDefault();
    const pastedData = e.clipboardData.getData("Text");

    // 하이픈(-)을 기준으로 분리 후, 앞뒤 공백 제거
    const splitted = pastedData.split("-").map((part: string) => part.trim());
    if (splitted.length !== 5) {
      setInvalidPasteFormat(true);
      return;
    }

    setFormData({
      text1: splitted[0],
      text2: splitted[1],
      text3: splitted[2],
      text4: splitted[3],
      text5: splitted[4],
    });

    setInvalidPasteFormat(false);
  };

  // 사용자가 직접 입력하는 경우에도 실시간 업데이트 (선택사항)
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value, // 해당 input의 name에 대응하는 값을 업데이트
    }));
  };

  return (
    <div style={{ padding: "1rem", fontFamily: "Arial, sans-serif" }}>
      <div className="flex gap-2">
        <Input
          className="bg-white"
          name="text1"
          type="text"
          value={formData.text1}
          onPaste={handlePaste}
          onChange={handleInputChange}
        />
        <Input
          className="bg-white"
          name="text2"
          type="text"
          value={formData.text2}
          onChange={handleInputChange}
        />
        <Input
          className="bg-white"
          name="text3"
          type="text"
          value={formData.text3}
          onChange={handleInputChange}
        />
        <Input
          className="bg-white"
          name="text4"
          type="text"
          value={formData.text4}
          onChange={handleInputChange}
        />
        <Input
          className="bg-white"
          name="text5"
          type="text"
          value={formData.text5}
          onChange={handleInputChange}
        />
        <Button
          onClick={() => {
            setFormData(initialState);
          }}
        >
          clear
        </Button>
      </div>
      <div>
        <p>
          {formData.text1}-{formData.text2}-{formData.text3}-{formData.text4}-
          {formData.text5}
        </p>
        {invalidPastedFormat && (
          <p>관리번호 형식이 틀립니다. (5개의 구분기호 분리)</p>
        )}
      </div>
    </div>
  );
}

export default HyphenSplitInputs;
