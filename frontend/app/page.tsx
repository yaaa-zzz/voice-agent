"use client";

import { useEffect, useState } from "react";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

export default function Home() {
  const [mounted, setMounted] = useState(false);
  const [reply, setReply] = useState("");
  const [latency, setLatency] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  if (!mounted) {
    return null;
  }

  if (!browserSupportsSpeechRecognition) {
    return (
      <main className="p-10">
        <h1 className="text-2xl font-bold">
          Browser does not support Speech Recognition
        </h1>
      </main>
    );
  }

  const startListening = () => {
    resetTranscript();

    SpeechRecognition.startListening({
      continuous: false,
      language: "en-IN",
    });
  };

  const stopListening = async () => {
    SpeechRecognition.stopListening();

    if (!transcript.trim()) {
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: transcript,
          }),
        }
      );

      const data = await response.json();

      console.log(data);

      setReply(data.reply || "No reply received");

      setLatency(
        data.latency_ms
          ? `${data.latency_ms} ms`
          : "N/A"
      );

      const speech = new SpeechSynthesisUtterance(
        data.reply
      );

      speech.lang = "en-IN";

      window.speechSynthesis.speak(speech);

    } catch (error) {
      console.error(error);

      setReply(
        "Failed to connect to backend."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-8">

      <h1 className="text-4xl font-bold mb-6">
        2Care AI Voice Agent
      </h1>

      <div className="space-x-4 mb-6">

        <button
          onClick={startListening}
          className="border px-4 py-2 rounded"
        >
          🎤 Start Listening
        </button>

        <button
          onClick={stopListening}
          className="border px-4 py-2 rounded"
        >
          📤 Stop & Send
        </button>

      </div>

      <div className="mb-4">
        <strong>Status:</strong>{" "}
        {listening
          ? "Listening..."
          : "Not Listening"}
      </div>

      <div className="mb-6">

        <h2 className="text-xl font-semibold">
          Transcript
        </h2>

        <div className="border p-4 rounded mt-2 min-h-[80px]">
          {transcript ||
            "Speak something..."}
        </div>

      </div>

      <div className="mb-6">

        <h2 className="text-xl font-semibold">
          Agent Reply
        </h2>

        <div className="border p-4 rounded mt-2 min-h-[80px]">

          {loading
            ? "Processing..."
            : reply ||
              "Waiting for response..."}

        </div>

      </div>

      <div>

        <h2 className="text-xl font-semibold">
          Latency
        </h2>

        <div className="border p-4 rounded mt-2">
          {latency || "N/A"}
        </div>

      </div>

    </main>
  );
  }