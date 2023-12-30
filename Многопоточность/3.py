import asyncio


async def main(filenames):
    names = []
    for filename in filenames:
        curr_names = await read_file_async(filename)
        names.append(curr_names)
    names_str = ' '.join(name for name in names)
    return names_str