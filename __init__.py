import json
import urllib.request

class GoogleDocUpdater:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "webhook_url": ("STRING", {"default": "PASTE_YOUR_APPS_SCRIPT_URL_HERE", "multiline": False}),
                "resume_text": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "update_doc"
    CATEGORY = "Custom/Text"

    def update_doc(self, webhook_url, resume_text):
        data = json.dumps({"content": resume_text}).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                url = res_data.get("url", "Success")
                return (url,)
        except Exception as e:
            return (f"ERROR: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "GoogleDocUpdater": GoogleDocUpdater
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "GoogleDocUpdater": "Google Doc Webhook Pusher"
}