//SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract MedicalRecords {
    struct MedicalRecord {
        bytes32 patientId;
        bytes32 doctorId;
        bytes32 hospitalId;
        bytes32 medicalHistory;
        bytes32 prescriptions;
        bytes32 testResults;
        bytes32 vaccinationRecords;
    }

    mapping(bytes32 => MedicalRecord) public medicalRecords;

    function createMedicalRecord(bytes32 _patientId, bytes32 _doctorId, bytes32 _hospitalId, bytes32 _medicalHistory, bytes32 _prescriptions, bytes32 _testResults, bytes32 _vaccinationRecords) public {
        MedicalRecord memory medicalRecord = MedicalRecord(_patientId, _doctorId, _hospitalId, _medicalHistory, _prescriptions, _testResults, _vaccinationRecords);
        medicalRecords[_patientId] = medicalRecord;
    }

    function updateMedicalRecord(bytes32 _patientId, bytes32 _medicalHistory, bytes32 _prescriptions, bytes32 _testResults, bytes32 _vaccinationRecords) public {
        MedicalRecord storage medicalRecord = medicalRecords[_patientId];
        medicalRecord.medicalHistory = _medicalHistory;
        medicalRecord.prescriptions = _prescriptions;
        medicalRecord.testResults = _testResults;
        medicalRecord.vaccinationRecords = _vaccinationRecords;
    }

    function getMedicalRecord(bytes32 _patientId) public view returns (MedicalRecord memory) {
        return medicalRecords[_patientId];
    }
}
