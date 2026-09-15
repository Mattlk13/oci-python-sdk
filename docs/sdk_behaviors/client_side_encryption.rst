.. _client-side-encryption:

Client-Side Encryption
~~~~~~~~~~~~~~~~~~~~~~

OCI Python SDK client-side encryption stores the KMS master key ID, vault ID,
and region in the encrypted blob. During decryption, this metadata is treated
as untrusted input and is validated before the SDK creates a new KMS client.

Pinned KMS master key provider
------------------------------

A ``KMSMasterKeyProvider`` created with a ``KMSMasterKey`` is pinned to that
key, vault, and region. It decrypts a blob only when the blob metadata matches
the configured master key. A mismatch raises ``ValueError`` locally; the
provider does not discover or create a different master key from the blob.

Decrypt-only KMS master key provider
------------------------------------

A ``KMSMasterKeyProvider`` created without a master key can discover the key
needed for decryption. Discovery proceeds only when the blob region is trusted
independently through one of these sources:

* The exact region in the provider configuration
* ``OCI_REGION``, when the provider configuration does not contain a region
* The active SDK region registry, including built-in and locally registered
  regions
* ``~/.oci/regions-config.json``
* ``OCI_REGION_METADATA``
* Instance Metadata Service (IMDS), only after the application explicitly
  enables the existing IMDS region lookup

An unknown region from the blob alone is rejected. Endpoint fallback for an
unknown region does not make that region trusted. Valid cross-region
decrypt-only use continues to work when the target region is known or
registered.

Migration guidance
------------------

If the blob uses the configured key, no change is needed. If your application
uses more than one key, create a pinned provider for each approved key and
select it using application data you trust. Alternatively, use a decrypt-only
provider and configure or register each allowed region.
