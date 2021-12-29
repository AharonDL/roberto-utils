import dtlpy as dl


def get_train_module(package_name: str):
    return dl.PackageModule(
        entry_point='roberto_utils_train.py',
        name=package_name + '-train',
        class_name='ServiceRunner',
        init_inputs=[],
        functions=[
            dl.PackageFunction(
                name='train_on_snapshot',
                display_name='train-on-snapshot-{}'.format(package_name),
                description="run train of the model on the specific snapshot id",
                inputs=[
                    dl.FunctionIO(type=dl.PackageInputType.SNAPSHOT, name='snapshot'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='cleanup'),
                ],
                outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='snapshot_id')]
            ),
            dl.PackageFunction(
                name='train_from_dataset',
                display_name='train-on-dataset-{}'.format(package_name),
                description="run train of a model on a raw dataset",
                inputs=[
                    dl.FunctionIO(type=dl.PackageInputType.DATASET, name='dataset'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='filters'),
                    dl.FunctionIO(type=dl.PackageInputType.SNAPSHOT, name='from_snapshot'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='snapshot_name'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='configuration'),
                ], outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='snapshot_id')]
            ),
            dl.PackageFunction(
                name='clone_snapshot_from_dataset',
                display_name='clone-from-dataset-{}'.format(package_name),
                description="clones the current scope to a new snapshot",
                inputs=[
                    dl.FunctionIO(type=dl.PackageInputType.DATASET, name='dataset'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='filters'),
                    dl.FunctionIO(type=dl.PackageInputType.SNAPSHOT, name='from_snapshot'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='snapshot_name'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='configuration'),
                ], outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='snapshot_id')]
            ),
            dl.PackageFunction(
                name='execution_wrapper',
                display_name='execution-wrapper-train-{}'.format(package_name),
                description="wrapper to all functions that support getting calls from UI",
                inputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='config')],
                outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='config')],
            )
        ])


def get_predict_module(package_name: str):
    return dl.PackageModule(
        entry_point='roberto_utils_predict.py',
        name=package_name + '-predict',
        class_name='ServiceRunner',
        init_inputs=[
            dl.FunctionIO(type="Json", name='project_name'),
            dl.FunctionIO(type="Json", name='project_id'),
            dl.FunctionIO(type="Json", name='model_name'),
            dl.FunctionIO(type="Json", name='model_id'),
            dl.FunctionIO(type="Json", name='snapshot_name'),
            dl.FunctionIO(type="Json", name='snapshot_id'),
        ],
        functions=[
            # dl.PackageFunction(
            #     name='predict',
            #     display_name='predict-{}'.format(package_name),
            #     inputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='dl_input')],
            #     outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='dl_input')],
            # ),
            dl.PackageFunction(
                name='predict_item',
                display_name='predict-item-{}'.format(package_name),
                description='predict a single item with the object adapter',
                inputs=[
                    dl.FunctionIO(type=dl.PackageInputType.ITEM, name='item'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='with_upload'),
                    dl.FunctionIO(type=dl.PackageInputType.JSON, name='with_return'),
                ],
                outputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM, name='item')],
            ),
            dl.PackageFunction(
                name='execution_wrapper',
                display_name='execution-wrapper-predict-{}'.format(package_name),
                description="wrapper to all functions that support getting calls from UI",
                inputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='config')],
                outputs=[dl.FunctionIO(type=dl.PackageInputType.JSON, name='config')],
            )
        ])
