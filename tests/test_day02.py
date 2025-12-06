# tests/test_day02.py
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from day02 import app  # import the FastAPI instance

client = TestClient(app)

class TestChatAPI(unittest.TestCase):

    @patch("day02.qa_pipeline")  # mock the pipeline correctly
    def test_chat_success(self, mock_pipeline):
        # Mock the pipeline's return value
        mock_pipeline.return_value = {"answer": "NLP libraries"}

        payload = {
            "question": "What does Hugging Face provide?",
            "context": "Hugging Face provides open-source NLP libraries ..."
        }

        response = client.post("/chat", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["answer"], "NLP libraries")

    @patch("day02.qa_pipeline")
    def test_chat_pipeline_error(self, mock_pipeline):
        # Simulate pipeline raising an exception
        mock_pipeline.side_effect = Exception("Pipeline failed")

        payload = {
            "question": "What does Hugging Face provide?",
            "context": "Some context"
        }

        response = client.post("/chat", json=payload)
        self.assertEqual(response.status_code, 500)
        self.assertIn("Pipeline failed", response.json()["detail"])


if __name__ == "__main__":
    unittest.main()
