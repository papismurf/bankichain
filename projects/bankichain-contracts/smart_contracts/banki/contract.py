import beaker as bk
import pyteal as pt


class ContractState:
    result = bk.GlobalStateValue(pt.TealType.bytes)


app = bk.Application("Banki", state=ContractState())


@app.external
def hello(name: pt.abi.String, *, output: pt.abi.String) -> pt.Expr:
    return output.set(pt.Concat(pt.Bytes("Hello, "), name.get()))


@app.external(read_only=True)
def set_result(*, result: pt.abi.Bytes) -> pt.Expr:
    return result.set(app.state.result)


if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")

