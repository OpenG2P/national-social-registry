-- ---------------------------------------------------------------------------
-- VC source views — read-only views that expose exactly the registry fields a
-- Verifiable Credential carries. Owned by the NSR extension so they deploy
-- automatically with the registry data model (applied by the db-seed job,
-- which runs all meta_data/**/*.sql after the model tables are migrated).
--
-- One view per VC type. The Agent Portal API reads these (phone-keyed) and
-- pushes the columns as VC claims. Column aliases MUST match the credential
-- template ${...} variables (quote camelCase to preserve case in Postgres).
--
-- To add another VC (e.g. socio-economic), add a sibling view here joining the
-- relevant tables, and add a matching VC definition in the registry Helm values
-- (agentPortalApi.vcDefinitions) + its credential_config.
-- ---------------------------------------------------------------------------

-- BeneficiaryIdCard — minimal identity credential.
-- One row per phone number (a person may have several; each maps 1:1 to them),
-- active records only.
-- `photo` = the MINIO OBJECT KEY of the registrant's photo (NOT the bytes). The
-- Agent Portal API fetches the object by this key, thumbnails it for the
-- claim-169 QR, and places it on the printed card. Adjust the source expression
-- to wherever your registry stores the photo reference (here: a `photo` document
-- key on the individual record; map to your actual column/jsonb path).
CREATE OR REPLACE VIEW public.beneficiary_vc_view AS
SELECT ph ->> 'number'              AS phone,
       i.functional_record_id       AS "functionalRecordId",
       i.full_name                  AS "fullName",
       to_char(i.birth_date, 'YYYY-MM-DD') AS "dateOfBirth",
       i.photo                      AS "photoKey"
FROM   public.g2p_register_individuals i,
       jsonb_array_elements(i.phone_numbers) ph
WHERE  i.record_status = 'ACTIVE';
