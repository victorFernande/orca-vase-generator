# Automatic OrcaCloud publishing / Publicação automática

Publishing a GitHub release sends its verified `_any.py` asset to the connected
OrcaCloud plugin automatically. Keep the repository connected under **Edit
plugin → GitHub publishing**. No stored OrcaCloud token is needed.

The service requires a release-triggered GitHub OIDC identity. A normal manual
Actions run or workflow-run callback does not provide that identity. The
publisher therefore stays in the original release job while waiting for the
released tag CI to pass, then obtains its short-lived credential and uploads.
It uses the documented curl client, with the credential on stdin rather than
in command arguments or files. Multipart JSON preserves semicolons and Unicode.

Before uploading it verifies the asset SHA-256, PEP 723 version and plugin
identity. A successful upload must return HTTP 201 and the expected plugin ID
and version, and stores `orcacloud-publish.json` on the GitHub release. Reruns
skip an identical already-confirmed publication only when this receipt matches.
If a transient failure occurs, rerun the **release publication** run in Actions,
retaining its release event context. Do not use a normal manual Actions run.

The workflow and helper must be present in the released tag. Changes to the
publisher should ship in a new patch release rather than moving published tags.
CI-created releases use GITHUB_TOKEN, which does not trigger release workflows.
The Box CI therefore prepares a draft when no release exists. Publish that
release through GitHub (web UI or an authorized account's CLI) after CI passes.
That one GitHub publication automatically updates OrcaCloud, with no Cloud upload.

Pull request tests have read-only permissions. OIDC and receipt writes belong
only to the release publisher. Publication confirmation does not replace native
OrcaSlicer or physical-print validation.

## Português

Ao **publicar uma release no GitHub**, o fluxo envia automaticamente o arquivo
`_any.py` verificado para o plugin conectado no OrcaCloud. O serviço exige que
esse envio parta do evento de publicação da release. O fluxo aguarda a CI da
tag mantendo esse contexto e obtém uma credencial temporária apenas ao enviar.

O comprovante `orcacloud-publish.json` registra plugin, versão e SHA-256. Para
repetir um envio interrompido, use **Re-run** na execução original de publicação
da release. Uma execução manual comum não fornece a identidade exigida.
O reparo do publicador precisa estar na tag de uma nova versão de correção.

No Box, a CI prepara um rascunho quando a release ainda não existe. Publique
esse rascunho no GitHub após os testes. Não é necessário carregar arquivos
manualmente no OrcaCloud. O vínculo do repositório permanece habilitado e os
próximos envios acontecem pela publicação da release, sem segredo armazenado.
