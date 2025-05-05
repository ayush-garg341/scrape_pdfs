import asyncio
from pyppeteer import connect


async def save_educative_lessons():
    # Connect to your Chrome instance
    browser = await connect(browserURL="http://127.0.0.1:9222")

    # Find the Educative tab
    pages = await browser.pages()
    page = None
    for p in pages:
        url = p.url
        if "educative.io" in url:
            page = p
            break

    if not page:
        print("❌ Educative tab not found.")
        return

    print(f"✅ Connected to: {page.url}")

    i = 48
    while True:
        # Wait for content to load
        await asyncio.sleep(4)

        # Save PDF
        filename = f"lesson_{i:02}.pdf"
        dimensions = await page.evaluate(
            """() => {
            return {
                width: document.documentElement.scrollWidth,
                height: document.documentElement.scrollHeight,
            }
        }"""
        )

        pdf_bytes = await page.pdf(
            {
                "path": filename,
                "width": f"{dimensions['width']}px",
                "height": f"{dimensions['height']}px",
                "printBackground": True,
                "margin": {
                    "top": "0px",
                    "bottom": "0px",
                    "left": "0px",
                    "right": "0px",
                },
            }
        )

        print(f"✅ Saved {filename}")

        i += 1

        # Try clicking the "Next Lesson" button
        try:
            await page.evaluate(
                """
                () => {
                    let btn = document.querySelector("button[aria-label='Next button']");
                    if (btn) btn.click();
                }
            """
            )
        except Exception as e:
            print("⚠️ Could not click next:", e)
            break

        await asyncio.sleep(10)  # Wait for next lesson to load

    await browser.disconnect()


asyncio.get_event_loop().run_until_complete(save_educative_lessons())
