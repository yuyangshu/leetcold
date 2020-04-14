class Solution:
    def entityParser(self, text: str) -> str:
        return (
            text.replace("&amp;", '&')
                .replace("&apos;", '\'')
                .replace("&frasl;", '/')
                .replace("&gt;", '>')
                .replace("&lt;", '<')
                .replace("&quot;", '"')
        )
