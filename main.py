import asyncio
import sys
import logging


logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')


async def process_number(number):
    """Aszinkron függvény, amely 1 másodperc várakozás után duplázza a számot."""
    logging.info(f"Feldolgozás: {number}")
    await asyncio.sleep(1)
    return number * 2


async def main():
    logging.info("Program elindult")

    raw_args = sys.argv[1:]
    numbers = []


    for arg in raw_args:
        try:
            num = float(arg)

            if num.is_integer():
                num = int(num)
            numbers.append(num)
        except ValueError:
            logging.error(f"A megadott paraméter nem szám: {arg}")

    if not numbers:
        return


    tasks = [process_number(n) for n in numbers]
    results = await asyncio.gather(*tasks)

    print(f"Eredmények: {results}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass