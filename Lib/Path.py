

class Path:
    def __init__(self, app_api, invoke, package, method) -> None:

        self.app_api = app_api
        self.invoke = invoke
        self.package = package
        self.method = method

    def meta_path_1(self):
        return self.app_api @ self.app_api.T

    def meta_path_2(self):
        return self.app_api @ self.method @ self.app_api.T

    def meta_path_3(self):
        return self.app_api @ self.package @ self.app_api.T

    def meta_path_4(self):
        return self.app_api @ self.invoke @ self.app_api.T

    def meta_path_5(self):
        return self.app_api @ self.method @ self.package @ self.app_api.T

    def meta_path_6(self):
        return self.app_api @ self.package @ self.method @ self.package.T @ self.app_api.T

    def meta_path_7(self):
        return self.app_api @ self.method @ self.invoke @ self.method.T @ self.app_api.T

    def meta_path_8(self):
        return self.app_api @ self.invoke @ self.method @ self.invoke.T @ self.app_api.T

    def meta_path_9(self):
        return self.app_api @ self.package @ self.invoke @ self.package.T @ self.app_api.T

    def meta_path_10(self):
        return self.app_api @ self.invoke @ self.package @ self.invoke.T @ self.app_api.T

    def meta_path_11(self):
        return self.app_api @ self.method @ self.package @ self.invoke @ self.package.T @ self.method.T @ self.app_api.T

    def meta_path_12(self):
        return self.app_api @ self.package @ self.method @ self.invoke @ self.method.T @ self.package.T @ self.app_api.T

    def meta_path_13(self):
        return self.app_api @ self.method @ self.invoke @ self.package @ self.invoke.T @ self.method.T @ self.app_api.T

    def meta_path_14(self):
        return self.app_api @ self.invoke @ self.method @ self.package @ self.method.T @ self.invoke.T @ self.app_api.T

    def meta_path_15(self):
        return self.app_api @ self.invoke @ self.package @ self.method @ self.package.T @ self.invoke.T @ self.app_api.T

    def meta_path_16(self):
        return self.app_api @ self.package @ self.invoke @ self.method @ self.invoke.T @ self.package.T @ self.app_api.T