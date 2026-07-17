class PipelineRegistry:
    def __init__(self):
        self.pipelines = {}

    def register(self, name, pipeline):
        self.pipelines[name] = pipeline

    def run(self, name):
        if name not in self.pipelines:
            raise ValueError(f"{name} not found")

        return self.pipelines[name].run()

    def list(self):
        return list(self.pipelines.keys())


registry = PipelineRegistry()
