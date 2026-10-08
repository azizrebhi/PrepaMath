import asyncio
import asyncpg


async def main():
    try:
        print("Connecting...")

        conn = await asyncpg.connect(
            user="postgres.csybihyyqgvfggdztwrr",
            password="YOUR_REAL_PASSWORD",
            host="34.241.16.247",
            port=5432,
            database="postgres",
            timeout=15,
            ssl="require",
        )

        print("✅ Connected successfully!")

        await conn.close()

    except Exception as e:
        print(f"❌ {type(e).__name__}: {repr(e)}")


asyncio.run(main())