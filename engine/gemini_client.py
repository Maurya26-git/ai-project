"""
Google Gemini LLM Integration Client
Provides deep contextual sentiment analysis, sarcasm detection, and actionable business insights.
"""
import os
import json
import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

class GeminiSentimentClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY", "")

    def is_available(self) -> bool:
        return bool(self.api_key and self.api_key.strip())

    def analyze_deep(self, text: str, api_key: str = None) -> dict:
        active_key = api_key or self.api_key
        if not active_key or not active_key.strip():
            return {
                "enabled": False,
                "message": "Gemini API key not configured. Enable in Settings to unlock deep LLM insights."
            }

        prompt = f"""
You are an expert NLP and customer sentiment intelligence engine. Analyze the sentiment of the following text with high precision.

TEXT TO ANALYZE:
\"\"\"{text}\"\"\"

Provide your response in strictly valid JSON format with this exact structure:
{{
  "overall_sentiment": "Positive" | "Negative" | "Neutral" | "Mixed",
  "confidence_percentage": 95,
  "executive_summary": "1-2 sentence high level summary of the user's emotional and practical stance.",
  "tone_descriptors": ["Enthusiastic", "Constructive", "Urgent"],
  "sarcasm_detected": false,
  "sarcasm_explanation": "Explanation of sarcasm/irony if present, otherwise null",
  "actionable_insights": [
    "Specific recommendation or takeaway for the business/support team"
  ],
  "nuance_highlights": [
    "Key subtleties or implicit expectations in the user's words"
  ]
}}
Ensure the output is solely valid parseable JSON. Do not include markdown code block backticks if possible, or wrap strictly in ```json.
"""

        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }

        url = f"{GEMINI_API_URL}?key={active_key.strip()}"

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=12)
            if resp.status_code != 200:
                return {
                    "enabled": False,
                    "error": f"Gemini API returned status {resp.status_code}: {resp.text[:150]}"
                }

            data = resp.json()
            candidates = data.get("candidates", [])
            if not candidates:
                return {"enabled": False, "error": "No candidates returned from Gemini API."}

            part_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            
            # Clean possible markdown fence
            clean_text = part_text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.startswith("```"):
                clean_text = clean_text[3:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]

            parsed = json.loads(clean_text.strip())
            parsed["enabled"] = True
            return parsed

        except requests.exceptions.Timeout:
            return {"enabled": False, "error": "Gemini API request timed out."}
        except Exception as e:
            return {"enabled": False, "error": f"Failed to call Gemini API: {str(e)}"}
