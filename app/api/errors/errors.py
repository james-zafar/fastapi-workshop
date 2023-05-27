from app.api.errors.error_response import Error


class ModelNotFoundError(Error):
    code = 'model_not_found'
    message = 'A model with the specified ID could not be located'
    status_code = 404


class ModelNotReadyError(Error):
    code = 'model_not_ready'
    message = 'Results are only available for models with a status of completed.' \
              'Use GET /models/{model_id} to monitor the status of the model.'
    status_code = 400


class BadConfigError(Error):
    code = 'bad_data_source'
    message = 'The data source specified could not be accessed. Please check the source and API key and try again.'
    status_code = 400


class InternalServerError(Error):
    code = 'internal_error'
    message = 'An internal error occurred.'
    status_code = 500
