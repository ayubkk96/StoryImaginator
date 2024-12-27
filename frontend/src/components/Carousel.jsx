import { useState } from "react";
import { jsPDF } from "jspdf";
import "../styles/Carousel.css";
import Actions from "./Actions";

const Carousel = ({ data }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [editMode, setEditMode] = useState(false);

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % data.length);
  };

  const handlePrev = () => {
    setCurrentIndex(
      (prevIndex) =>
        (prevIndex - 1 + data.length) % data.length
    );
  };

  const handleSave = () => {};

  const handleEdit = () => {};

  const handleDownload = () => {
    const doc = new jsPDF();
    const story = data[currentIndex];
    const storyText = `Title: ${story.currentIndex}\nPrompt: ${
      story.prompt
    }\nurl:\n${story.url
      .map((criteria) => "\u2022 " + criteria)
      .join("\n")}`;
    const lines = doc.splitTextToSize(storyText, 180);
    doc.text(lines, 10, 10);

    doc.setProperties({
      title: story.currentIndex,
    });

    doc.save(`${story.currentIndex}.pdf`);
  };

  const handleDownloadAll = () => {
    const doc = new jsPDF();
    data.user_stories.forEach((story, index) => {
      const storyText = `Title: ${story.index}\nPrompt: ${
        story.prompt
      }\nurl:\n${story.url
        .map((criteria) => "\u2022 " + criteria)
        .join("\n")}`;
      const lines = doc.splitTextToSize(storyText, 180);
      doc.text(lines, 10, 10);
      if (index < data.length - 1) {
        doc.addPage();
      }
    });

    doc.setProperties({
      title: "All Stories",
    });

    doc.save("all_stories.pdf");
  };

  return (
    <div className="carousel-parent">
      <div className="actions-parent">
        <Actions
          handleDownload={handleDownload}
          handleEdit={handleEdit}
          handleSave={handleSave}
          editMode={editMode}
          setEditMode={setEditMode}
        />
      </div>
      <div className="left-arrow" onClick={handlePrev}>
        &#8592;
      </div>
      <div className={editMode ? "edit-text-item" : "text-item"}>
        <div key={data[currentIndex]}>
          <h2 id="card-title">
            <>
              <b></b> {data[currentIndex].prompt}
            </>
          </h2>

          <p id="card-description">
          <b></b>   <img src={data[currentIndex].url} alt="cat" />
          </p>
        </div>
      </div>
      <div className="right-arrow" onClick={handleNext}>
        &#8594;
      </div>
      <div className="footer">
        <div className="pagination">
          {data.map((_, index) => (
            <span
              key={index}
              className={`dot ${index === currentIndex ? "active" : ""}`}
              onClick={() => setCurrentIndex(index)}
            ></span>
          ))}
        </div>
        <div className="download-all-button" onClick={handleDownloadAll}>
          Download All
        </div>
      </div>
    </div>
  );
};

export default Carousel;
