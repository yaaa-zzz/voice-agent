import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "2Care AI Voice Agent",
  description: "Healthcare Appointment Booking Assistant",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}