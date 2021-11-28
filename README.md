# What is it?

Explorations of crime that is happening in MTL, QC, Canada.

## Structure

- [MontrealCrime Notebook](./MontrealCrime.nb)
  - Notebook that generates series of images that are saved under `data_viz/` folder.
- [to_mp4.py](./to_mp4.py)
  - Code that is used to generate an MP4 based from `data_viz/` folder.

## Usage

- To run `MontrealCrime.nb` you would need to get Wolfram Language subscription.

  - Although, the same files can be generate in `Python`, it took me less time to program in WL. (Although the runtime is orders lengthier that what it could be in `Python`, I saved time and pain figuring out how to do it in `Python` )

- `to_mp4.py` 

  - To run this you need to install `pipenv`
    - You can also check `Pipfile` and install libraries with `pip`

  ```bash
  pipenv install # installs all the dependencies
  pipenv shell # activates venv
  python to_mp4.py # generates movie.mp4
  ```

