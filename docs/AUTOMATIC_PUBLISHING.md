# Automatic OrcaCloud publishing / Publicação automática

Publishing a GitHub release automatically publishes its verified `_any.py`
asset to the connected OrcaCloud plugin. Connect this repository once under
**Edit plugin → GitHub publishing**. No stored OrcaCloud token is needed.

The publisher waits for successful CI on the exact released commit. It also
listens for successful tag CI, because a release created by `GITHUB_TOKEN`
does not itself trigger another release workflow. To recover a missed upload,
run **Publish to OrcaCloud → Run workflow** on `main` and enter the existing
release tag. This recovery never rebuilds or changes the published package.

Before uploading, the publisher checks the release asset's SHA-256, PEP 723
version and plugin identity. JSON is encoded as a real multipart field so
semicolons, quotes and Unicode in the changelog remain valid. A successful
upload stores `orcacloud-publish.json` on the GitHub release. Replays with the
same version, package and plugin are skipped only when that receipt matches.

The publisher job alone has OIDC and release-write permissions. Pull request
tests cannot upload. A rejection from OrcaCloud fails visibly; success requires
the API to confirm the expected plugin ID and version. Browser, native slicer
and physical printing checks remain separate from publication confirmation.

## Português

Ao publicar uma release no GitHub, o fluxo envia automaticamente o arquivo
`_any.py` já verificado para o plugin conectado no OrcaCloud. Conecte o
repositório uma vez em **Editar plugin → GitHub publishing**. O envio usa
credenciais temporárias do GitHub, sem segredo OrcaCloud armazenado.

O fluxo aguarda a CI do commit publicado e também acompanha a conclusão da
CI da tag. Para recuperar uma publicação pendente, execute **Publish to
OrcaCloud → Run workflow** em `main`, informando a tag existente. O pacote
publicado não é reconstruído. O comprovante `orcacloud-publish.json` registra
plugin, versão e SHA-256 e evita repetir uma publicação já confirmada.

Uma rejeição do OrcaCloud aparece como falha. Publicação confirmada exige que
a API devolva o ID do plugin e a versão esperados; isso não substitui testes
dentro do OrcaSlicer nem validação física das peças.
